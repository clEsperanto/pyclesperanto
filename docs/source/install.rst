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

    conda recipe is not yet available


From source
====================

Alternatively, you can also install the latest development version from GitHub and build it from source. 
First start by cloning the repository:

.. code-block:: bash

    git clone https://github.com/clEsperanto/pyclesperanto.git
    cd pyclesperanto

Then, create a virtual environment:

.. code-block:: bash

    conda create --name myenv python='3.10' -c conda-forge
    conda activate myenv

and install the dependencies:

.. code-block:: bash

    pip install -r requirements.txt

Once all is set, install the package locally with pip:

.. code-block:: bash

    pip install . -vvv

.. note::
    
    The ``-e`` flag is not supported yet. The ``-vvv`` flag is optional and enables verbose output.

Running then ``pytest`` command will run the test suite. If all tests pass, you are ready to go!
