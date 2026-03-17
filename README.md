# pyclesperanto

[![Image.sc Forum](https://img.shields.io/badge/dynamic/json.svg?label=forum&amp;url=https%3A%2F%2Fforum.image.sc%2Ftags%2Fpyclesperanto.json&amp;query=%24.topic_list.tags.0.topic_count&amp;colorB=green&amp;&amp;suffix=%20topics&amp;logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAABPklEQVR42m3SyyqFURTA8Y2BER0TDyExZ+aSPIKUlPIITFzKeQWXwhBlQrmFgUzMMFLKZeguBu5y+//17dP3nc5vuPdee6299gohUYYaDGOyyACq4JmQVoFujOMR77hNfOAGM+hBOQqB9TjHD36xhAa04RCuuXeKOvwHVWIKL9jCK2bRiV284QgL8MwEjAneeo9VNOEaBhzALGtoRy02cIcWhE34jj5YxgW+E5Z4iTPkMYpPLCNY3hdOYEfNbKYdmNngZ1jyEzw7h7AIb3fRTQ95OAZ6yQpGYHMMtOTgouktYwxuXsHgWLLl+4x++Kx1FJrjLTagA77bTPvYgw1rRqY56e+w7GNYsqX6JfPwi7aR+Y5SA+BXtKIRfkfJAYgj14tpOF6+I46c4/cAM3UhM3JxyKsxiOIhH0IO6SH/A1Kb1WBeUjbkAAAAAElFTkSuQmCC)](https://forum.image.sc/tag/pyclesperanto)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pyclesperanto.svg)](https://anaconda.org/conda-forge/pyclesperanto)
[![PyPI](https://img.shields.io/pypi/v/pyclesperanto.svg?color=green)](https://pypi.org/project/pyclesperanto)
[![License](https://img.shields.io/pypi/l/pyclesperanto.svg?color=green)](https://github.com/clEsperanto/pyclesperanto/blob/main/LICENSE)
[![Development Status](https://img.shields.io/pypi/status/pyclesperanto.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![Build](https://github.com/clEsperanto/pyclesperanto/actions/workflows/build.yml/badge.svg)](https://github.com/clEsperanto/pyclesperanto/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/clesperanto/pyclesperanto/branch/main/graph/badge.svg)](https://codecov.io/gh/clesperanto/pyclesperanto)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13853800.svg)](https://doi.org/10.5281/zenodo.13853800)

__pyclesperanto__ is the python package of [clEsperanto] - a multi-language framework for GPU-accelerated image processing.
It relies on a familly of [OpenCL kernels] originated from [CLIJ].
This python package uses [PyBind11] to wrap the C++ [CLIc] library as a processing backend.

## Installation, Documentation, and Uses

To install pyclesperanto from `pip`:
```bash
pip install pyclesperanto
```

Please, refere to the [documentation] for full installation instructions and options, guides, and examples on how to use the pyclesperanto.
If you encountering any difficulties or have questions we encourage you to raise them on the [image.sc forum] under the tag `clesperanto`,
or to open a [github issue](https://github.com/clEsperanto/pyclesperanto/issues).

## __Code Example__

```python
import pyclesperanto as cle
from skimage.io import imread, imsave

# initialize GPU
device = cle.select_device()
print("Used GPU: ", device)

image = imread("https://samples.fiji.sc/blobs.png?raw=true")

# push image to device memory
input_image = cle.push(image)

# process the image
inverted = cle.subtract_image_from_scalar(input_image, scalar=255)
blurred = cle.gaussian_blur(inverted, sigma_x=1, sigma_y=1)
binary = cle.threshold_otsu(blurred)
labeled = cle.connected_components_labeling(binary)

# The maxmium intensity in a label image corresponds to the number of objects
num_labels = cle.maximum_of_all_pixels(labeled)

# print out result
print("Num objects in the image: " + str(num_labels))

# read image from device memory
output_image = cle.pull(labeled)
imsave("result.tif", output_image)
```

## __Examples & Demos__

<table border="0">
<tr><td>
<img src="docs/demos/images/select_device.png" width="300"/>
</td><td>

* [Select and Manage devices](docs/demos/api/select_devices.ipynb)
* [Host-Device memory management](docs/demos/api/push_pull_create.ipynb)
* [Process an image](docs/demos/api/process_image.ipynb)

</td></tr>

<tr><td>
<img src="docs/demos/images/crop_and_paste_images.png" width="300"/>
</td><td>

* [Crop, Flip, Paste arrays](docs/demos/basics/crop_flip_paste.ipynb)
* [Math operations](docs/demos/basics/arithmetic_operators.ipynb)
* [Matrix operations](docs/demos/basics/matrices_operations.ipynb)
* [Vector and Matrix operations](docs/demos/basics/vectors_and_matrices_operations.ipynb)
* [How to inspecting 3D image](docs/demos/basics/inspecting_3d_images.ipynb)

</td></tr>


<tr><td>
<img src="docs/demos/images/segmentation_3d.png" width="300"/>
</td><td>

* [Segment and analyse blobs](docs/demos/examples/analyse_blobs.ipynb)
* [Voronoi-Otsu labeling](docs/demos/examples/voronoi_otsu_labeling.ipynb)
* [Cell segmentation based on membrane](docs/demos/examples/membrane_segmentation_2d.ipynb)
* [Cell segmentation in 3D](docs/demos/examples/Segmentation_3D.ipynb)

</td></tr>


<tr><td>
<img src="docs/demos/images/affine_transforms.png" width="300"/>
</td><td>

* [Edge detection](docs/demos/examples/edge_detection_and_enhancement.ipynb)
* [Ridge and Tube detection](docs/demos/examples/ridge_detection.ipynb)
* [Parametric maps](docs/demos/examples/parametric_maps.ipynb)
* [Rotation, scaling, translation, and affine transform](docs/demos/examples/affine_transforms.ipynb)
<!-- * [Morphomathic operations](https://github.com/clEsperanto/pyclesperanto/tree/main/docs/demos/examples/morphomath_operation.ipynb)   -->

</td></tr>


<tr><td>
<img src="docs/demos/images/multi-device-tiling.png" width="300"/>
</td><td>

* [Multi-device tile processing](docs/demos/examples/multi-gpu_tile_processing_with_dask.ipynb)
* [Ask Bia-Bob example](docs/demos/interoperability/biabob-example.ipynb)

</td></tr>

</table>

More usage and example can be found as notebooks in the [tutorial section](https://clesperanto-doc.readthedocs.io/en/latest/docs/pyclesperanto/tutorials.html) of the documentation as well as in the [docs/demos](https://github.com/clEsperanto/pyclesperanto/tree/main/docs/demos) folder of the repository.

# __Contributing and Feedback__

[clEsperanto](https://github.com/clEsperanto) is developed in the open because we believe in the [open source community](https://clij.github.io/clij2-docs/community_guidelines).
Feel free to drop feedback as [github issue](https://github.com/clEsperanto/pyclesperanto/issues) or via [image.sc](https://image.sc). Contributions, of any kind, are very welcome. Feel free to reach out to us. And if you liked our work, star the repository, share it with your friends, and use it to make cool stuff!

## Acknowledgements

We acknowledge support by the Deutsche Forschungsgemeinschaft under Germany’s Excellence Strategy (EXC2068) Cluster of Excellence Physics of Life of TU Dresden and by the [Institut Pasteur, Paris](https://www.pasteur.fr/en). This project has been made possible in part by grant number 2021-237734 ([GPU-accelerating Fiji and friends using distributed CLIJ, NEUBIAS-style, EOSS4](https://chanzuckerberg.com/eoss/proposals/gpu-accelerating-fiji-and-friends-using-distributed-clij-neubias-style/)) from the Chan Zuckerberg Initiative DAF, an advised fund of the Silicon Valley Community Foundation, and by support from the French National Research Agency via the [France BioImaging research infrastructure](https://france-bioimaging.org/) (ANR-24-INBS-0005 FBI BIOGEN).

[clEsperanto]: http://clesperanto.net/
[OpenCL kernels]: https://github.com/clEsperanto/clij-opencl-kernels/tree/clesperanto_kernels
[CLIJ]: http://clij.github.io/
[CLIc]: https://github.com/clEsperanto/CLIc
[community guidelines]: https://clij.github.io/clij2-docs/community_guidelines
[github issue]: https://github.com/clEsperanto/pyclesperanto/issues
[image.sc forum]: https://forum.image.sc/tag/clesperanto/1556
[PyBind11]: https://github.com/pybind
[documentation]: https://clesperanto-doc.readthedocs.io/en/latest/docs/pyclesperanto/index.html
