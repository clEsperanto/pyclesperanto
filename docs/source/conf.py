# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pyclesperanto'
copyright = '2023, Stephane Rigaud'
author = 'Stephane Rigaud'
release = '0.6.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
  'sphinx.ext.autodoc',  # Parses (sub)modules
  'sphinx.ext.napoleon',  # Parses Numpy docstrings
  'sphinx.ext.mathjax',  # Print mathematical expressions
  'nbsphinx',  # link notebooks
  'sphinx.ext.autosummary',  # Make module lists in table
]

templates_path = ['_templates']
exclude_patterns = ['build', '_build', 'Thumbs.db', '.DS_Store']

autodoc_mock_imports = ["pyclesperanto._pyclesperanto", "toolz", "matplotlib", "numpy"]
add_module_names = False
modindex_common_prefix = ['pyclesperanto.']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' # 'alabaster'
html_static_path = ['_static']
