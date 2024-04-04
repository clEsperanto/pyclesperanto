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


connected_components_labeling_box
----------------------------------

``connected_components_labeling_box`` was renamed to ``connected_components_labeling`` and now as a parameter ``connectivity``.
The argument ``connectivity`` is a string that can be either ``box`` or ``sphere``.
This was discussed in the `issue #142 <https://github.com/clEsperanto/pyclesperanto/issues/142>`__.
This connectivity management may be applied to other similar function in the future.

.. code-block:: python

    import pyclesperanto as cle

    gpu_output = cle.connected_components_labeling(gpu_input, connectivity="box")

