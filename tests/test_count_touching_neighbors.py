import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_count_touching_neighbors():
    labels = cle.push(
        np.asarray(
            [
                [1, 1, 0, 3, 3],
                [1, 1, 2, 3, 3],
                [0, 2, 2, 2, 0],
                [4, 4, 2, 5, 5],
                [4, 4, 0, 5, 5],
            ]
        )
    )

    reference = cle.push(np.asarray([0, 1, 4, 1, 1, 1]))

    touch_matrix = cle.generate_touch_matrix(labels)

    neighbor_count_vector = cle.count_touching_neighbors(touch_matrix)

    a = cle.pull(neighbor_count_vector)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_count_touching_neighbors_not_ignoring_background():
    labels = cle.push(
        np.asarray(
            [
                [1, 1, 0, 3, 3],
                [1, 1, 2, 3, 3],
                [0, 2, 2, 2, 0],
                [4, 4, 2, 5, 5],
                [4, 4, 0, 5, 5],
            ]
        )
    )

    reference = cle.push(np.asarray([5, 2, 5, 2, 2, 2]))

    touch_matrix = cle.generate_touch_matrix(labels)

    neighbor_count_vector = cle.count_touching_neighbors(
        touch_matrix, ignore_background=False
    )

    a = cle.pull(neighbor_count_vector)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
