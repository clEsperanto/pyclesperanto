Contributing
############

pyclesperanto is a Python API layer for the `CLIc library <https://github.com/clEsperanto/CLIc>`__.
Several operation and functionality are directly inherited from the CLIc library, compiled and imported in the package as ``_clesperanto``.
Arround this C++ core, the package as several Python code to ensure proper integration with the Python ecosystem (numpy, etc.).

Therefore, it is possible to contribute to the development of py-clesperanto either on the C++ side or on the Python side depending on what you are trying to achieve.

Environment setup
------------------

To contribute to the development of pyclesperanto, you will need to install it from the source code.
Please follow the `installation guide <install.rst>`__ to install the package from source.

Also for code cleaness, we strongly advise to install the pre-commit hooks to ensure code quality and style.

.. code-block:: bash

    pip install pre-commit
    pre-commit install

New python operations
---------------------

Algorithm implementation of the library is destined to be in C++. However, C++ development can be tedious and difficult, and its integration into CLIc can be complex.
Therefore, it is possible to implement new operations in Python, and provid it to the python package in the  ``__future__`` or ``__interroperability__`` module of the package.

Once stable and tested, we will be happy to fully integrate the operation to the C++ side of the library for full deployement.

New OpenCL operations
---------------------

(WIP)

Versioning
----------

pyclesperanto version folows the `CLIc <https://github.com/clEsperanto/CLIc>`__ versioning for now as both are development concurently.
Although they are not necessarily made to be identically, the versioning is kept in sync as much as possible.

In order to update the version of pyclesperanto, or the version of CLIc, modify the `_version.py` file of pyclesperanto package.

`VERSION` define the versioning tag of the package `pyclesperanto`. It should be updated when a new release is made.
`CLIC_VERSION` define the `CLIc <https://github.com/clEsperanto/CLIc>`__ library version to use.

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
