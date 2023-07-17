# import pyclesperanto as cle
# import matplotlib.pyplot as plt
# import numpy as np

# def test_create():
#     cle.create((10,10,10), dtype=float)
#     cle.create((10,10), dtype=int)
#     cle.create((10,), dtype=np.int8)

# def test_create_like():
#     cle.create_like(np.asarray([[1,2,3],[4,5,6]]))

# def test_push():
#     cle.push(np.asarray([[1,2,3],[4,5,6]]))
#     cle.push(np.asarray([[1,2,3],[4,5,6]]).astype(np.int16), mtype=cle.buffer)
#     cle.push(np.asarray([[1,2,3],[4,5,6]]).astype(np.float32), mtype=cle.image)

# def test_pull():
#     gpu1 = cle.push(np.asarray([[1,2,3],[4,5,6]]).astype(np.int16), mtype=cle.buffer)
#     gpu2 = cle.push(np.asarray([[1,2,3],[4,5,6]]).astype(np.float32), mtype=cle.image)
#     cle.pull(gpu1)
#     cle.pull(gpu2)

