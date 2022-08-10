# import numpy as np
# from typing import Union
# import inspect
# from typing import Callable
# from functools import wraps
# from toolz import curry

# from ._pyclic import data

# Image = Union[np.ndarray, data]

# def is_image(object):
#     return isinstance(object, np.ndarray) or \
#            isinstance(object, tuple) or \
#            isinstance(object, list) or \
#            isinstance(object, data) or \
#            str(type(object)) in ["<class 'cupy._core.core.ndarray'>",
#                                  "<class 'dask.array.core.Array'>",
#                                  "<class 'xarray.core.dataarray.DataArray'>"]


# @curry
# def plugin_function(
#     function: Callable,
# ) -> Callable:
#     """Function decorator to ensure correct types and values of all parameters.

#     The given input parameters are either of type OpenCL data/image/buffer (which the GPU
#     understands) or are converted to this type (see push function). If output
#     parameters of type Image are not set, an empty image is created and
#     handed over.

#     Parameters
#     ----------
#     function : callable
#         The function to be executed on the GPU.

#     Returns
#     -------
#     worker_function : callable
#         The actual function call that will be executed, magically creating
#         output arguments of the correct type.
#     """

#     @wraps(function)
#     def worker_function(*args, **kwargs):
#         sig = inspect.signature(function)
#         # create mapping from position and keyword arguments to parameters
#         # will raise a TypeError if the provided arguments do not match the signature
#         # https://docs.python.org/3/library/inspect.html#inspect.Signature.bind
#         bound = sig.bind(*args, **kwargs)
#         # set default values for missing arguments
#         # https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.apply_defaults
#         bound.apply_defaults()

#         myself = args[0]

#         # copy images to GPU, and create output array if necessary
#         for key, value in bound.arguments.items():
#             if is_image(value) and key in sig.parameters and sig.parameters[key].annotation is Image:
#                 bound.arguments[key] = myself.push(value)
#             if key in sig.parameters and sig.parameters[key].annotation is Image and value is None:
#                 sig2 = inspect.signature(myself.create_like)
#                 bound.arguments[key] = myself.create_like(*bound.args[1:len(sig2.parameters) + 1])

#         # call the decorated function
#         return function(*bound.args, **bound.kwargs)

#     # this is necessary to obfuscate pyclesperanto's internal structure
#     worker_function.__module__ = "pyclesperanto_prototype"

#     return worker_function
