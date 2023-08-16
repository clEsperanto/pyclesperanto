Installation
############

From package manager
====================

The Installation of pyClesperanto can be done via pip:

.. code-block:: bash

    pip install pyclesperanto

or via conda:

.. code-block:: bash

    conda install -c conda-forge pyclesperanto

.. warning::

    conda recipe is not yet available, please use pip for now.

.. note::

    It is advised to install pyClesperanto in a virtual environment. For example, you can create a new environment with conda:

    .. code-block:: bash
            
        conda create --name myenv python='3.10' -c conda-forge
        conda activate myenv


From source
====================

Alternatively, you can also install the latest version from GitHub and build it from source on your system. 
First start by cloning the repository:

.. code-block:: bash

    git clone https://github.com/clEsperanto/pyclesperanto.git
    cd pyclesperanto

Then, create a virtual environment:

.. code-block:: bash

    conda create --name myenv python='3.10' -c conda-forge
    conda activate myenv

and install the package from the source:

.. code-block:: bash

    pip install .

.. note::
    
    The ``-e`` flag is not supported yet. 

.. note::

    You can add the flag ``-vvv`` to enables verbose output of the build process.

pyClesperanto should now be installed in your virtual environment along with all its dependencies.