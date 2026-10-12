"""The bindings release the GIL during CLIc calls (see dask_plan_P0_gil_release.md).

- the GIL is free while a GPU operation runs, so other Python threads progress
- concurrent calls from several threads on the *same* device give the same
  results as sequential calls (CLIc thread safety: program cache, OpenCL kernel
  arguments, Metal command buffers)
"""

import threading
import time

import numpy as np

import pyclesperanto as cle

N_THREADS = 8
N_ITERATIONS = 50


def _run_threads(target, n):
    errors = []

    def wrapped(i):
        try:
            target(i)
        except Exception as e:  # report exceptions raised in the threads
            errors.append((i, repr(e)))

    threads = [threading.Thread(target=wrapped, args=(i,)) for i in range(n)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return errors


def test_gil_released_during_gpu_work(gpu_backend):
    device = cle.select_device()
    image = cle.push(
        np.random.default_rng(0).random((2000, 2000), dtype=np.float32), device=device
    )

    def run():
        cle.gaussian_blur(image, sigma_x=15, sigma_y=15).get()

    for _ in range(3):
        run()  # warm-up: kernel compilation

    ticks = [0]
    stop = threading.Event()

    def spin():
        while not stop.is_set():
            ticks[0] += 1

    spinner = threading.Thread(target=spin)
    spinner.start()
    time.sleep(0.2)

    before = ticks[0]
    start = time.perf_counter()
    for _ in range(20):
        run()
    elapsed = time.perf_counter() - start
    during = ticks[0] - before

    before = ticks[0]
    time.sleep(elapsed)
    idle = ticks[0] - before

    stop.set()
    spinner.join()

    # with the GIL held during the calls the spinner gets ~30% of its idle rate
    ratio = during / idle
    assert ratio > 0.6, f"spinner ran at {ratio:.0%} of its idle rate"


def test_same_device_concurrent_filters(gpu_backend):
    device = cle.select_device()
    rng = np.random.default_rng(1)
    images = [rng.random((256, 256), dtype=np.float32) for _ in range(N_THREADS)]

    def compute(i, image):
        gpu = cle.push(image, device=device)
        # each thread uses different scalar arguments for the same kernels
        blurred = cle.gaussian_blur(gpu, sigma_x=1 + i, sigma_y=1 + i)
        top_hat = cle.top_hat(blurred, radius_x=1 + i, radius_y=1 + i)
        added = cle.add_image_and_scalar(top_hat, scalar=float(i))
        return added.get(), cle.sum_of_all_pixels(added)

    references = [compute(i, images[i]) for i in range(N_THREADS)]

    def worker(i):
        for _ in range(N_ITERATIONS):
            result, total = compute(i, images[i])
            assert np.array_equal(
                result, references[i][0]
            ), f"thread {i}: image differs"
            assert total == references[i][1], f"thread {i}: sum differs"

    assert not _run_threads(worker, N_THREADS)


def test_same_device_concurrent_labeling(gpu_backend):
    device = cle.select_device()
    rng = np.random.default_rng(2)
    images = [
        (rng.random((256, 256)) * 255).astype(np.uint8) for _ in range(N_THREADS // 2)
    ]

    def compute(i):
        labels = cle.voronoi_otsu_labeling(
            cle.push(images[i], device=device), spot_sigma=1 + i, outline_sigma=1
        )
        return labels.get()

    references = [compute(i) for i in range(len(images))]

    def worker(i):
        for _ in range(N_ITERATIONS // 5):
            assert np.array_equal(
                compute(i), references[i]
            ), f"thread {i}: labels differ"

    assert not _run_threads(worker, len(images))


def test_same_device_concurrent_transfers(gpu_backend):
    device = cle.select_device()
    rng = np.random.default_rng(3)
    images = [rng.random((512, 512), dtype=np.float32) for _ in range(N_THREADS)]

    def worker(i):
        for _ in range(N_ITERATIONS):
            gpu = cle.push(images[i], device=device)
            assert np.array_equal(gpu.get(), images[i])
            region = np.asarray(gpu[10:100, 20:200])  # region read
            assert np.array_equal(region, images[i][10:100, 20:200])

    assert not _run_threads(worker, N_THREADS)
