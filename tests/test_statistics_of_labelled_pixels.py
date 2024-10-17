import numpy as np

import pyclesperanto as cle


def test_statistics_of_labelled_pixels():

    labels = cle.push(
        np.asarray(
            [
                [1, 1, 1, 2, 2, 2],
                [1, 1, 1, 2, 2, 2],
                [1, 1, 1, 2, 2, 2],
                [3, 3, 3, 4, 4, 4],
                [3, 3, 3, 4, 4, 4],
                [3, 3, 3, 4, 4, 4],
            ]
        )
    )

    intensities = cle.push(
        np.asarray(
            [
                [14, 4, 4, 3, 3, 13],
                [4, 0, 4, 3, 0, 3],
                [4, 4, 4, 3, 3, 3],
                [2, 2, 2, 1, 1, 1],
                [2, 0, 2, 1, 0, 1],
                [12, 2, 2, 1, 1, 11],
            ]
        )
    )

    result = cle.statistics_of_labelled_pixels(intensities, labels)

    print(result)

    assert result["label"] == [1.0, 2.0, 3.0, 4.0]
    assert result["max_intensity"] == [14.0, 13.0, 12.0, 11.0]
    assert result["min_intensity"] == [0.0, 0.0, 0.0, 0.0]
    assert np.allclose(
        np.asarray(result["mean_intensity"]),
        np.asarray(
            [
                4.666666507720947,
                3.777777910232544,
                2.8888888359069824,
                2.0,
            ]
        ),
        atol=0.00001,
    )
    assert result["sum_intensity"] == [42.0, 34.0, 26.0, 18.0]
    assert result["area"] == [9.0, 9.0, 9.0, 9.0]
