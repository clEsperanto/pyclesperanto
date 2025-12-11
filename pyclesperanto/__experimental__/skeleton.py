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
    device: Optional[Device] = None,
) -> Image:

    edges = binary_subtract(input_image, binary_erode(input_image))
    nb_edges = (int) (sum_of_all_pixels(edges))
    print(f"Number of max pixel candidates in the input image: {nb_edges}")

    if output_image is None:
        output_image = Array.to_device(np.zeros((3,nb_edges)))
    counter = Array.to_device(np.asarray([0]))

    params = {
            "src": edges,
            "dst": output_image,
            "idx": counter,
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


@plugin_function
def skeleton(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:

    flag = Array.to_device(np.asarray([0]))
    output_image = Array.empty_like(input_image)
    temp_image = Array.zeros_like(input_image)

    copy(input_image, temp_image)


    nb_edges = sum_of_all_pixels(input_image - binary_erode(input_image)) / maximum_of_all_pixels(input_image)
    print(f"Number of max pixel candidates in the input image: {nb_edges}")



    dimension = len(input_image.shape)
    max_direction = 6 if dimension > 2 else 4
    flip_flag = True
    unchanged_border = 0


    while unchanged_border < max_direction:
        unchanged_border = 0

        for d in range(max_direction):

            flag.fill(0)
            if flip_flag:
                params = {
                    "src": temp_image,
                    "flag_dst": flag,
                    "dst": output_image,
                    "direction": d+1,
                    "dimension": dimension,
                }
            else:
                params = {
                    "src": output_image,
                    "flag_dst": flag,
                    "dst": temp_image,
                    "direction": d+1,
                    "dimension": dimension,
                }

            execute(
                anchor=__file__,
                kernel_source="skeleton_x.cl",
                kernel_name="skeletonize",
                device=device,
                global_size=input_image.shape,
                parameters=params,
            )


            # we may need to have a temp data that list the pixels to remove and remove them sequentially

            flip_flag = not flip_flag
            if flag.get()[0] == 0:
                unchanged_border += 1


    if flip_flag:
        copy(temp_image, output_image)


    return output_image  # Return the final skeleton and the flag value

