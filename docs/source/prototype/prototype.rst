Prototype migration
===================

This document is intended to help users to migrate their code from the prototype to the current version of the library.
Most changes concern function names and arguments names or order. We try to keep as much as possible legacy compatibility, but some changes were not possible to avoid.

.. note::

    This document is not exhaustive and may not cover all changes.
    Please refer to the `repository issues <https://github.com/clEsperanto/pyclesperanto/issues>`__ for more information.
    And feel free to open an issue if you have any question or if you think something is missing.

Library import
--------------

The import of the library was changed from ``import pyclesperanto_prototype as cle`` to ``import pyclesperanto as cle``.

.. tabs::

    .. tab:: pyclesperanto

        .. code-block:: python

            import pyclesperanto as cle

    .. tab:: prototype

        .. code-block:: python

            import pyclesperanto_prototype as cle



`imread` & `imwrite`
--------------------

``imread`` and ``imwrite`` were removed from the library as they are redondant with other libraries such as `scikit-image`.
Please rely on these libraries to read and write images. This was discussed in the `issue #140 <https://github.com/clEsperanto/pyclesperanto/issues/140>`__.

.. code-block:: python

    from skimage.io import imread, imwrite

    image = imread('image.png')
    gpu_image = cle.push(image)


erode_labels
------------

``erode_labels`` arguments ``relabeled_island`` was renamed to ``relabel`` for more sense.
This was discussed in the `issue #141 <https://github.com/clEsperanto/pyclesperanto/issues/141>`__.

.. tabs::

    .. tab:: pyclesperanto

        .. code-block:: python

            gpu_output = cle.erode_labels(gpu_input, radius=1, relabel=False)

    .. tab:: prototype

        .. code-block:: python

            gpu_output = cle.erode_labels(gpu_input, radius=1, relabeled_island=False)


Filter connectivity management
------------------------------

We removed the connectivity from the filters names (e.g. ``connected_components_labeling_box`` and ``connected_components_labeling_diamond``)
and updated the filters to have it as a parameter (e.g. ``connected_component_labeling``), using the ``box`` as default value.

.. tabs::

    .. tab:: pyclesperanto

        .. code-block:: python

            gpu_output = cle.connected_component_labeling(gpu_input, connectivity="box")
            gpu_output = cle.connected_component_labeling(gpu_input, connectivity="sphere")

    .. tab:: prototype

        .. code-block:: python

            gpu_output = cle.connected_components_labeling_box(gpu_input, connectivity="box")
            gpu_output = cle.connected_components_labeling_sphere(gpu_input, connectivity="sphere")


We unified the connectivity name to be either ``box`` or ``sphere``, and applied this to all filters that have a connectivity parameter.
This was discussed in the `issue #142 <https://github.com/clEsperanto/pyclesperanto/issues/142>`__.

List of filters that were changed (the list may not be exhaustive):

- ``connected_components_labeling_box`` -> ``connected_components_labeling``
- ``connected_components_labeling_diamond`` -> ``connected_components_labeling``
- ``laplace_box`` -> ``laplace_filter``
- ``laplace_diamond`` -> ``laplace_filter``
- ``maximum_box`` -> ``maximum_filter``
- ``maximum_sphere`` -> ``maximum_filter``
- ``mean_box`` -> ``mean_filter``
- ``mean_sphere`` -> ``mean_filter``
- ``median_box`` -> ``median_filter``
- ``median_sphere`` -> ``median_filter``
- ``minimum_box`` -> ``minimum_filter``
- ``minimum_sphere`` -> ``minimum_filter``
- ``nonzero_minimum_box`` -> ``nonzero_minimum``
- ``nonzero_minimum_sphere`` -> ``nonzero_minimum``
- ``nonzero_maximum_box`` -> ``nonzero_maximum``
- ``nonzero_maximum_sphere`` -> ``nonzero_maximum``
- ``variance_box`` -> ``variance_filter``
- ``variance_sphere`` -> ``variance_filter``
- ``standard_deviation_box`` -> ``standard_deviation``
- ``standard_deviation_sphere`` -> ``standard_deviation``

Legacy name are still available but will be removed in future versions. Deprecation warnings will be raised.

Affine transform
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

Morphological operations
------------------------

The `prototype` library had a set of morphological operations for grayscale and binary images. However, the operations name, parameters, and organisation were not consistent accross grayscale and binary.
This was discussed in this `issue <https://github.com/clEsperanto/CLIc/issues/385>__`.

binary images:
 - dilate_box & dilate_sphere -> binary_dilate and take a connectivity parameter and a radius parameter for x, y, and z.
 - erode_box & erode_sphere -> binary_erode and take a connectivity parameter and a radius parameter for x, y, and z.
grayscale images:
 - minimum_box & minimum_sphere -> minimum_filter and take a connectivity parameter and a radius parameter for x, y, and z.
 - maximum_box & maximum_sphere -> maximum_filter and take a connectivity parameter and a radius parameter for x, y, and z.
 - opening_box & opening_sphere -> grayscale_opening and take a connectivity parameter and a radius parameter for x, y, and z.
 - closing_box & closing_sphere -> grayscale_closing and take a connectivity parameter and a radius parameter for x, y, and z.

We also introduce a `binary_opening` and `binary_closing` operation that rely on the `binary_dilate` and `binary_erode` operations.
These operations uses a box or sphere shape footprint only. For custom footprint, please use the `dilation` and `erosion` operations.
