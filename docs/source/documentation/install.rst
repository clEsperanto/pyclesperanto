Installation
############

From Package Manager (Recommended)
==================================

pyclesperanto is available on PyPI and conda-forge, and can be installed via pip or conda. It is recommended to install it via a package manager to ensure that all dependencies are correctly installed.

.. tabs::

    .. tab:: Pip

        Install from PyPI with `pip`:

        .. code-block:: bash

            pip install pyclesperanto

    .. tab:: Conda

        Install from conda-forge with `conda` or `mamba`:

        .. code-block:: bash

            conda install -c conda-forge pyclesperanto

.. note::

    It is strongly advised to install pyclesperanto in a virtual environment. For example, you can create a new environment with conda:

    .. code-block:: bash

        conda create --name myenv
        conda activate myenv

.. warning::

    Installing pyclesperanto with mamba or conda on MacOS or Linux will require an additional package to be installed to see compatible OpenCL platforms.

    .. tabs::

        .. tab:: MacOS

            .. code-block:: bash

                conda install -c conda-forge ocl_icd_wrapper_apple

        .. tab:: Linux

            .. code-block:: bash

                conda install -c conda-forge ocl-icd-system

From Source
===========

Alternatively, you can install the package from source on your system. This is not advised unless you are planning to contribute to the development of the package, test new features, or debug issues.
We strongly recommend using a virtual environment to install the package from source.

Run the following commands in your terminal to install the package from source:

.. code-block:: bash

    git clone https://github.com/clEsperanto/pyclesperanto.git
    cd pyclesperanto
    pip install .

.. note::

    You can add the flag ``-v`` to enable verbose output of the build process.

.. warning::

    The ``-e`` flag is advised if you are planning to contribute to the development of the package.

pyclesperanto should now be installed as a package along with all its dependencies. You can now start using it in your Python scripts and test modifications to the source code.
However, any modification of the source code will require you to re-install the package with `pip` to take effect.

Troubleshooting
===============

In case of error messages such as ``"No OpenCL platform found"``, you may need to install the OpenCL drivers for your system or ``"clGetPlatformIDs failed: PLATFORM_NOT_FOUND_KHR"``,
you may need to install more recent drivers for your GPU or you may be missing some specific libraries.
If you have issues, contact us for help on the `image.sc forum <https://forum.image.sc/>`__ or create an issue on the `GitHub repository <https://github.com/clEsperanto/pyclesperanto>`__.
