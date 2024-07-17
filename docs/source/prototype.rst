Prototype migration
===================

This document is intended to help users to migrate their code from the prototype to the current version of the library.
We mainly focus on change of function names or arguments.
Possible changes of position in the library are not covered here as they are not expected to be affecting the user code.

.. note::

    This document is not exhaustive and may not cover all changes.
    Please refer to the `repository issues <https://github.com/clEsperanto/pyclesperanto/issues>`__ for more information.
    And feel free to open an issue if you have any question or if you think something is missing.

import
------

The import of the library was changed from ``import pyclesperanto_prototype as cle`` to ``import pyclesperanto as cle``.

.. code-block:: python

    import pyclesperanto as cle


imread/imwrite
--------------

``imread`` and ``imwrite`` were removed from the library.
Please rely on an third-party library to read images, such as `scikit-image` or `tifffile` for example.
This was discussed in the `issue #140 <https://github.com/clEsperanto/pyclesperanto/issues/140>`__.

.. code-block:: python

    from skimage.io import imread, imwrite

    image = imread('image.png')
    gpu_image = cle.push(image)


erode_labels
------------

``erode_labels`` arguments ``relabeled_island`` was renamed to ``relabel`` for more sense.
This was discussed in the `issue #141 <https://github.com/clEsperanto/pyclesperanto/issues/141>`__.

.. code-block:: python

    import pyclesperanto as cle

    gpu_output = cle.erode_labels(gpu_input, radius=1, relabel=False)


filter connectivity management
------------------------------

We removed the connectivity from the filters names (e.g. ``connected_components_labeling_box`` and ``connected_components_labeling_diamond``)
and updated the filters to have it as a parameter (e.g. ``connected_components_labeling``).
We also unified the connectivity name to be either ``box`` or ``sphere``. The default is ``box`` for all filters.
This was discussed in the `issue #142 <https://github.com/clEsperanto/pyclesperanto/issues/142>`__.

.. code-block:: python

    import pyclesperanto as cle

    gpu_output = cle.connected_components_labeling(gpu_input, connectivity="box")
    gpu_output = cle.connected_components_labeling(gpu_input, connectivity="sphere")


List of filters that were changed (the list may not be exhaustive):

- ``connected_components_labeling_box`` -> ``connected_components_labeling``
- ``connected_components_labeling_diamond`` -> ``connected_components_labeling``
- ``laplace_box`` -> ``laplace``
- ``laplace_diamond`` -> ``laplace``
- ``maximum_box`` -> ``maximum``
- ``maximum_sphere`` -> ``maximum``
- ``mean_box`` -> ``mean``
- ``mean_sphere`` -> ``mean``
- ``median_box`` -> ``median``
- ``median_sphere`` -> ``median``
- ``minimum_box`` -> ``minimum``
- ``minimum_sphere`` -> ``minimum``
- ``nonzero_minimum_box`` -> ``nonzero_minimum``
- ``nonzero_minimum_sphere`` -> ``nonzero_minimum``
- ``nonzero_maximum_box`` -> ``nonzero_maximum``
- ``nonzero_maximum_sphere`` -> ``nonzero_maximum``
- ``variance_box`` -> ``variance``
- ``variance_sphere`` -> ``variance``
- ``standard_deviation_box`` -> ``standard_deviation``
- ``standard_deviation_sphere`` -> ``standard_deviation``


affine transform
----------------

We have updated the ``affine_transform`` arguments names:

- ``transform`` -> ``transform_matrix``
- ``linear_interpolation`` -> ``interpolate``
- ``auto_size`` -> ``resize``

The argument name change is to support more explicit names and to avoid confusion. The ``auto_size`` argument was changed to ``resize`` to be more explicit.
The ``linear_interpolation`` argument was changed to ``interpolate`` to be more flexible. For now only ``linear`` and ``nearest_neighbor`` are supported, hence the use of a ``boo``.
Future versions may support more interpolation methods. ``transformation`` argument was changed to ``transform_matrix`` to be more explicit as we expect a matrix as input.
``prototype`` allowed a ``numpy.ndarray`` or ``AffineTransform3D`` and ``AffineTransform`` object directly. However, we have drop compatibility with ``AffineTransform3D`` and ``AffineTransform`` objects.
For technical reason, we now only support 1D list of 9 or 16 elements.
