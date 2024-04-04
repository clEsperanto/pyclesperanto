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




