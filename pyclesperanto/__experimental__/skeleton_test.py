from typing import Optional

from pyclesperanto._array import Array, Image
from pyclesperanto._core import Device
from pyclesperanto._decorators import plugin_function
from pyclesperanto._functionalities import execute

from pyclesperanto._tier1 import copy, binary_erode, binary_subtract
from pyclesperanto._tier2 import sum_of_all_pixels, absolute_difference, maximum_of_all_pixels

import numpy as np



@plugin_function
def edge_coordinates(
    input_image: Image,
    output_image: Optional[Image] = None,
    direction: int = 1,
    device: Optional[Device] = None,
) -> Image:

    edges = binary_subtract(input_image, binary_erode(input_image))
    nb_edges = (int) (sum_of_all_pixels(edges))

    if output_image is None:
        output_image = Array.to_device(np.ones((3,nb_edges)) * -1)
    counter = Array.to_device(np.asarray([0]))

    params = {
            "src": edges,
            "dst": output_image,
            "idx": counter,
            "direction": direction,
        }

    execute(
        anchor=__file__,
        kernel_source="collect_coordinates.cl",
        kernel_name="collect_coordinates",
        device=device,
        global_size=input_image.shape,
        parameters=params
    )

    return output_image


# @plugin_function
# def edge_coordinates(
#     input_image: Image,
#     output_image: Optional[Image] = None,
#     device: Optional[Device] = None,
# ) -> Image:

#     edges = binary_subtract(input_image, binary_erode(input_image))
#     nb_edges = (int) (sum_of_all_pixels(edges))
#     print(f"Number of max pixel candidates in the input image: {nb_edges}")

#     if output_image is None:
#         output_image = Array.to_device(np.zeros((3,nb_edges)))
#     counter = Array.to_device(np.asarray([0]))

#     params = {
#             "src": edges,
#             "dst": output_image,
#             "idx": counter,
#         }

#     execute(
#         anchor=__file__,
#         kernel_source="collect_coordinates.cl",
#         kernel_name="collect_coordinates",
#         device=device,
#         global_size=input_image.shape,
#         parameters=params
#     )

#     return output_image


@plugin_function
def euler_invariant(
    input_image: Image,
    coord_list: Image,
    output_list: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:

    if output_list is None:
        output_list = Array.to_device(np.ones((3,coord_list.shape[-1])) * -1)

    params = {
        "src": coord_list,
        "img": input_image,
        "dst": output_list,
    }

    execute(
        anchor=__file__,
        kernel_source="euler_invariant.cl",
        kernel_name="euler_invariant",
        device=device,
        global_size=(coord_list.shape[-1],),
        parameters=params
    )

    return output_list


@plugin_function
def end_point(
    input_image: Image,
    coord_list: Image,
    output_list: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:

    if output_list is None:
        output_list = Array.to_device(np.ones((3,coord_list.shape[-1])) * -1)

    params = {
        "src": coord_list,
        "img": input_image,
        "dst": output_list,
    }

    execute(
        anchor=__file__,
        kernel_source="end_point.cl",
        kernel_name="end_point",
        device=device,
        global_size=(coord_list.shape[-1],),
        parameters=params
    )

    return output_list



@plugin_function
def simple_point(
    input_image: Image,
    coord_list: Image,
    output_list: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:

    if output_list is None:
        output_list = Array.to_device(np.ones((3,coord_list.shape[-1])) * -1)

    params = {
        "src": coord_list,
        "img": input_image,
        "dst": output_list,
    }

    execute(
        anchor=__file__,
        kernel_source="simple_point.cl",
        kernel_name="simple_point",
        device=device,
        global_size=(coord_list.shape[-1],),
        parameters=params
    )

    return output_list





@plugin_function
def skeleton(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """
    This function is a placeholder for the skeleton functionality.
    It should be implemented in the future.
    """

    if output_image is None:
        output_image = Array.zeros_like(input_image)

    res = np.zeros(input_image.shape)

    max_border = 7 if len(input_image.shape) == 3 else 5
    for direction in range(1, max_border):
        candidates = edge_coordinates(input_image, direction=direction)
        candidates = end_point(input_image, candidates)
        candidates = euler_invariant(input_image, candidates)
        candidates = simple_point(input_image, candidates)

        list_points = candidates.get()
        for c in range(list_points.shape[-1]):
            x,y,z =  list_points[:,c]
            if x == -1:
                continue
            if len(res.shape) == 2:
                res[int(y),int(x)] = 1
            else:
                res[int(z), int(y),int(x)] = 1

    return input_image - res


