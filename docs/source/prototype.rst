Prototype migration
===================

List of changes to be made in order to migrate from the prototype to the current version of the library.

imread
------

``imread`` was removed from the library. Please rely on an third-party library to read images, such as `scikit-image` for example.
This was discussed in the `issue #140 <https://github.com/clEsperanto/pyclesperanto/issues/140>`__.

.. code-block:: python

    from skimage.io import imread

    image = imread('image.png')
    gpu_image = cle.push(image)

