# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import re
import sys
from typing import Any, Dict

import yaml
from sphinx.locale import _

sys.path.insert(0, os.path.abspath("../../"))

# Open the CMakeCache.txt file and search for the project version
with open("../../pyclesperanto/_version.py", "r") as f:
    for line in f:
        if line.startswith("VERSION ="):
            start = line.find("=") + 1
            release = line[start:].strip().strip('"')
            break

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "pyclEsperanto"
slug = re.sub(r"\W+", "-", project.lower())
author = "Stephane Rigaud"
copyright = f"2024, {author}"
language = "en"
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    "sphinx.ext.autodoc",  # Parses (sub)modules
    "sphinx.ext.napoleon",  # Parses Numpy docstrings
    "sphinx.ext.mathjax",  # Print mathematical expressions
    "nbsphinx",  # link notebooks
    "sphinx.ext.autosummary",  # Make module lists in table
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "nbsphinx",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "sphinxemoji.sphinxemoji",
]

templates_path = ["_templates"]
exclude_patterns = ["build", "_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

autodoc_mock_imports = ["pyclesperanto._pyclesperanto", "toolz", "matplotlib", "numpy"]
add_module_names = False
modindex_common_prefix = ["pyclesperanto."]
gettext_compact = False
master_doc = "index"
suppress_warnings = ["image.nonlocal_uri"]
pygments_style = "friendly"
nbsphinx_execute = "never"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"  # 'alabaster'
html_theme_options = {
    "logo_only": False,
    "navigation_depth": 5,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "version_selector": True,
}

html_logo = "./images/logo_d_small.png"
# html_favicon = "demo/static/favicon.ico"
html_show_sourcelink = True
htmlhelp_basename = slug

html_static_path = ["_static"]
html_template_path = ["_templates"]

# -- Options for versionning ------------------------------------------------

# get the environment variable build_all_docs and pages_root
build_all_docs = os.environ.get("build_all_docs")
pages_root = os.environ.get("pages_root", "")

# if not there, we dont call this
if build_all_docs is not None:
    # we get the current language and version
    current_language = os.environ.get("current_language")
    current_version = os.environ.get("current_version")

    # we set the html_context wit current language and version
    # and empty languages and versions for now
    html_context: Dict[str, Any] = {
        "current_language": current_language,
        "languages": [],
        "current_version": current_version,
        "versions": [],
    }

    # and we append all versions and langauges accordingly
    # we treat t he main branch as latest
    if current_version == "main":
        html_context["languages"].append(["en", pages_root])

    if current_language == "en":
        html_context["versions"].append(["main", pages_root])

    # and loop over all other versions from our yaml file
    # to set versions and languages
    with open("versions.yaml", "r") as yaml_file:
        docs = yaml.safe_load(yaml_file)

    if docs:
        if current_version != "main":
            for language in docs[current_version].get("languages", []):
                html_context["languages"].append(
                    [language, pages_root + "/" + current_version + "/" + language]
                )
        for version, details in docs.items():
            html_context["versions"].append(
                [version, pages_root + "/" + version + "/" + current_language]
            )
