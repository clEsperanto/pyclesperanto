Installation
############

From package manager
====================

The Installation of pyClesperanto can be done via pip:

.. code-block:: bash

    pip install pyclesperanto

or via conda:

.. code-block:: bash

    mamba install -c conda-forge pyclesperanto

.. note::

    It is strongly advised to install pyClesperanto in a virtual environment. For example, you can create a new environment with conda:

    .. code-block:: bash

        mamba create --name myenv
        mamba activate myenv

.. note:: 

    It is often require to also install an additional package to use pyClesperanto, especially on MacOS or Linux:

    .. code-block:: bash

        mamba install ocl-icd-system

    .. code-block:: bash

        mamba install ocl_icd_wrapper_apple


In case of error messages such as ``"No OpenCL platform found", you may need to install the OpenCL drivers for your system."`` or ``"clGetPlatformIDs failed: PLATFORM_NOT_FOUND_KHR"``,
you may need to install more recent drivers for your GPU. Or you maybe missing some specific libraries. We advise you to check the Troubleshooting section of the documentation, and if
you still have issues, to contact us for help on the `image.sc forum <https://forum.image.sc/>` or creating an issue on the `github repository <https://github.com/clEsperanto/pyclesperanto>`.


From source
====================

Alternatively, you can also install the latest version from GitHub and build it from source on your system.
First start by cloning the repository:

.. code-block:: bash

    git clone https://github.com/clEsperanto/pyclesperanto.git
    cd pyclesperanto

Then, create a virtual environment:

.. code-block:: bash

    mamba create --name myenv
    mamba activate myenv

and install the package from the source:

.. code-block:: bash

    pip install .

.. note::

    You can add the flag ``-vvv`` to enables verbose output of the build process.

.. warning::

    The ``-e`` flag is not supported yet.


pyClesperanto should now be installed in your virtual environment as a package along with all its dependencies. You can now start using it in your Python scripts and test modifications to the source code.
However, any modification of the source code will require you to re-install the package with `pip` to take effect.

.. warning::

    If using an install from source, do not import the package from the source directory as it will not work properly.    
