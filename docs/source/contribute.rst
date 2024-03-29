Contributing
############

.. warning::

    This section of the documentation in under construction.


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