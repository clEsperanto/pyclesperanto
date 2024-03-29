import pyclesperanto as cle
import numpy as np

def test_label_bounding_box_2d():

    test = cle.push(np.asarray([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 0],
        [0, 0, 0, 0, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]))

    bb = cle.label_bounding_box(test, label_id=1)
    print(bb)

    assert bb[1] == 1
    assert bb[0] == 1

    assert bb[4] == 2
    assert bb[3] == 2