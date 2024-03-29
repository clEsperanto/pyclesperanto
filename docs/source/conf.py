# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import re

from sphinx.locale import _
sys.path.insert(0, os.path.abspath("../../"))

# Open the CMakeCache.txt file and search for the project version
with open('../../pyclesperanto/_version.py', 'r') as f:
    for line in f:
        if 'VERSION_CODE' in line:
            start = line.find('=') + 1
            end = line.find('\n', start)
            release = ".".join(line[start:end].strip().split(', '))
            break

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = u"py-clEsperanto"
slug = re.sub(r'\W+', '-', project.lower())
author = u'Stephane Rigaud'
copyright = f'2024, {author}'
language = 'en'
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    "sphinx.ext.autodoc",  # Parses (sub)modules
    "sphinx.ext.napoleon",  # Parses Numpy docstrings
    "sphinx.ext.mathjax",  # Print mathematical expressions
    "nbsphinx",  # link notebooks
    "sphinx.ext.autosummary",  # Make module lists in table
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

templates_path = ["_templates"]
exclude_patterns = ["build", "_build", "Thumbs.db", ".DS_Store"]

autodoc_mock_imports = ["pyclesperanto._pyclesperanto", "toolz", "matplotlib", "numpy"]
add_module_names = False
modindex_common_prefix = ["pyclesperanto."]
gettext_compact = False
master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # 'alabaster'
html_theme_options = {
    'logo_only': False,
    'navigation_depth': 5,
    'display_version': True,
    'collapse_navigation': False,
}
html_context = {}

if not 'READTHEDOCS' in os.environ:
    html_static_path = ['_static/']
    html_js_files = ['debug.js']

    # Add fake versions for local QA of the menu
    html_context['test_versions'] = list(map(
        lambda x: str(x / 10),
        range(1, 100)
    ))

# html_logo = "demo/static/logo-wordmark-light.svg"
html_show_sourcelink = True
# html_favicon = "demo/static/favicon.ico"
htmlhelp_basename = slug

latex_documents = [
  ('index', '{0}.tex'.format(slug), project, author, 'manual'),
]

man_pages = [
    ('index', slug, project, [author], 1)
]

texinfo_documents = [
  ('index', slug, project, author, slug, project, 'Miscellaneous'),
]

html_static_path = ['_static']

# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field

    app.add_object_type(
        'confval',
        'confval',
        objname='configuration value',
        indextemplate='pair: %s; configuration value',
        doc_field_types=[
            PyField(
                'type',
                label=_('Type'),
                has_arg=False,
                names=('type',),
                bodyrolename='class'
            ),
            Field(
                'default',
                label=_('Default'),
                has_arg=False,
                names=('default',),
            ),
        ]
    )