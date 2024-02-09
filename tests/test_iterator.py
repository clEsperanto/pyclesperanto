import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_iterator():
    image = np.random.random((3, 2, 5))
    cle_image = cle.asarray(image)
    print(image)
    print(cle_image)

    assert cle.array_equal(image, cle_image)

    for i, j in zip(image, cle_image):
        print(cle.array_equal(i, j))
        assert cle.array_equal(i, j)


def test_enumerate():
    cle_array = cle.create((2, 10))
    cle.set_ramp_x(cle_array)

    sum_ = 0
    for i, y in enumerate(cle_array[0]):
        print(i, y)
        sum_ += y

    assert sum_ == 45


def test_zip():
    cle_array = cle.create((2, 10))
    cle.set_ramp_x(cle_array)

    sum_ = 0
    for x, y in zip(cle_array[0], cle_array[1]):
        print(x, y)
        sum_ += y

    assert sum_ == 45


# def test_iter_centroids():
#     labels = cle.asarray(
#         [
#             [0, 0, 0, 0, 0],
#             [0, 1, 0, 3, 0],
#             [0, 0, 0, 0, 0],
#             [0, 0, 2, 0, 0],
#             [0, 0, 0, 0, 0],
#         ]
#     )

#     centroids = cle.centroids_of_labels(labels)

#     print(centroids)

#     for i, j in zip(centroids[0], centroids[1]):
#         print(i, j)
