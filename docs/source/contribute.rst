Contributing
############

.. warning::

    This section of the documentation in under construction.


py-clesperanto is a Python API layer for the `CLIc library <https://github.com/clEsperanto/CLIc>`__.
Several operation and functionality are directly inherited from the CLIc library, compiled and imported in the package as ``_clesperanto``.
Arround this C++ core, the package as several Python code to ensure proper integration with the Python ecosystem (numpy, etc.).

Therefore, it is possible to contribute to the development of py-clesperanto either on the C++ side or on the Python side depending on what you are trying to achieve.

Environment setup
------------------

Like for any other python development we encourage you to use a virtual environment to develop py-clesperanto.
Here we will describe how to setup a development environment for py-clesperanto with `conda/mamba`.

1. Create a new environment with `conda/mamba`:

.. code-block:: bash

    mamba create -n pycle-dev python=3.9 -c conda-forge
    conda activate pycle-dev

2. Install the dependencies:

.. code-block:: bash

    mamba install -c conda-forge numpy pytest jupyter scikit-image black flake8 pre-commit

3. Setup pre-commit:

.. code-block:: bash

    pre-commit install

4. Install py-clesperanto in development mode:

.. code-block:: bash

    pip install . -v

5. Run the tests:

.. code-block:: bash

    pytest

All tests should pass.
The ``pip install`` command will compile and install the package in the environment.
You will now be able to modify the ``pyclesperanto`` package and see the changes directly in the environment.
The ``pre-commit`` tool will ensure that the code is properly formatted and linted before any commit.

.. warning::

    ``-e`` flag of the ``pip install`` command is not available for the moment.


Versioning
----------

pyClesperanto version folows the `CLIc <https://github.com/clEsperanto/CLIc>`__ versioning.
Although they are not necessarily made to be identically, the versioning is kept in sync as much as possible.

In order to update the version of pyClesperanto, you will need to follow the following steps:

1. Update the `CLIc version tag <https://github.com/clEsperanto/pyclesperanto/blob/825ab6595b254bcda4fda81c03d2e7ff354f6dd2/CMakeLists.txt#L26>`__ used in the ``CMakeLists.txt`` file at the root of the project.
2. Update the version in the `pyproject.toml <https://github.com/clEsperanto/pyclesperanto/blob/main/pyproject.toml>`__ file.
3. Update the version in the `pyclesperanto/_version.py <https://github.com/clEsperanto/pyclesperanto/blob/main/pyclesperanto/_version.py>`__ file.
   Both ``VERSION`` and ``CLIC_VERSION`` should be updated accordingly.

.. note::

    The version tag in the ``pyproject.toml`` file should be made automatic in the near future.


Code quality and formating
--------------------------

The repository uses `pre-commit <https://pre-commit.com/>`__ to enforce code quality and style.
The configuration is stored in the `.pre-commit-config.yaml` file at the root of the project.
We are using the following hooks:
- `black <https://github.com/psf/black>`__ for code formatting
- `isort <https://pycqa.github.io/isort/>`__ for import sorting
- `flake8 <https://flake8.pycqa.org/en/latest/>`__ for code linting
in addition to more classical cleaning hooks like `end-of-file-fixer` and `trailing-whitespace`.

You can install the pre-commit hooks locally (see `pre-commit installation <https://pre-commit.com/>`__), allowing you to run the checks before committing your changes.
Otherwise, any pull request will automatically run the checks on the pre-commit CI.

.. note::

    `mypy <https://mypy.readthedocs.io/en/stable/>`__ is not yet integrated in the pre-commit hooks, but it is aleardy used and is planned to be added in the future.
