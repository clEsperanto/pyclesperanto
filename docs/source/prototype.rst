Prototype migration
===================

List of changes to be made in order to migrate from the prototype to the current version of the library.


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
- ``median_box`` -> ``median`
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
