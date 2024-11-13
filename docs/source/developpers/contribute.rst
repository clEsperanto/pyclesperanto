Contributing
############

pyclesperanto is a Python API layer for the `CLIc library <https://github.com/clEsperanto/CLIc>`__.
Several operation and functionality are directly inherited from the CLIc library, compiled and imported in the package as ``_clesperanto``.
Arround this C++ core, the package as several Python code to ensure proper integration with the Python ecosystem (numpy, etc.).

It is possible to contribute to the development of pyclesperanto either on the C++ side (see `CLIc Documentation <>`__) and on the Python side (pyclesperanto).
Developement on pyclesperanto can target new operations, new functionalities, bug fixes, code improvement, or documentation.

Environment setup
------------------

To contribute to the development of pyclesperanto, you will need to install it from the source code.
Please follow the `installation guide <install.rst>`__ to install the package from source. Additional packages maybe requiered to run tests, like ``pytest`` or ``scikit-image``.

Contributing to the python bindings
-----------------------------------

While most of the implementation is done in C++, we are also very interested in improving the Python API and developing new functions exclusively in Python.
Proposed new operations can be implemented in the ``__future__`` module of the package. Once stable and tested, we will fully integrate the operation into the package or migrate it to the C++ side of the library for full deployment.
API improvements are also welcome and can be discussed in issues or pull requests.
Additionally, any bug fixes, code improvements, documentation updates, typo corrections, etc., are highly appreciated.

New OpenCL operations (WIP)
---------------------

pyclesperanto provide two method for executing custom OpenCL code: `execute <>`_ and `native_execute <>`_.


Versioning
----------

pyclesperanto version folows the `CLIc <https://github.com/clEsperanto/CLIc>`__ versioning for now as both are development concurently.
Although they are not necessarily made to be identical, the versioning is kept in sync as much as possible. This may change in the future.

Update of version number in pyclesperanto is done in the `_version.py` file of pyclesperanto package, by updating the `VERSION` value.
The `CLIC_VERSION` variable refer to the `CLIc <https://github.com/clEsperanto/CLIc>`__ library tag to use for building the bindings.
It should not be modified unless you are directly updating code on the CLIc side.

.. note::

    `CLIC_VERSION` can also be set to an active branch name for development testing.


Code quality and formating
--------------------------

The repository uses `pre-commit <https://pre-commit.com/>`__ to enforce code quality and style.
The configuration is stored in the `.pre-commit-config.yaml` file at the root of the project.
We are using the following hooks:
- `black <https://github.com/psf/black>`__ for code formatting
- `isort <https://pycqa.github.io/isort/>`__ for import sorting
- `flake8 <https://flake8.pycqa.org/en/latest/>`__ for code linting
in addition to more classical cleaning hooks like `end-of-file-fixer` and `trailing-whitespace`.

You can install the pre-commit hooks locally (see `pre-commit installation <https://pre-commit.com/>`__), allowing you to run the checks before committing your changes:

.. code-block:: bash

    pip install pre-commit
    pre-commit install

Otherwise, any pull request will automatically run the checks on the pre-commit CI.

.. note::

    `mypy <https://mypy.readthedocs.io/en/stable/>`__ is not yet integrated in the pre-commit hooks, but it is aleardy used and is planned to be added in the future.
