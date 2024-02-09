import pyclesperanto as cle
import numpy as np

cle.select_device("TX")

source = np.asarray([0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0])
reference = np.asarray([0, 1, 0, 2, 0, 0, 3, 4, 0, 0, 5, 0])


def block_enum(source, blocksize):
    flagged_indices = cle.push(source)
    max_label = source.shape[0] - 1

    block_sums = cle.create([int((int(max_label) + 1) / blocksize) + 1])
    cle.sum_reduction_x(flagged_indices, block_sums, blocksize)

    # distribute new numbers
    new_indices = cle.create([int(max_label) + 1])
    cle.block_enumerate(flagged_indices, block_sums, new_indices, blocksize)

    return cle.pull(new_indices)


def test_block_enumerate():
    result = block_enum(source, 4)
    print(result)
    print(reference)
    assert np.array_equal(result, reference)

    result = block_enum(source, 2)
    print(result)
    print(reference)
    assert np.array_equal(result, reference)
