# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

project = "sz-sdk-python-grpc"
copyright = "2025, Senzing"
author = "senzing"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]


# -- Customization -----------------------------------------------------------

sys.path.insert(0, os.path.abspath("../../src"))
sys.path.insert(0, os.path.abspath("../../src/senzing_grpc/pb2_grpc"))


extensions = [
    "autodocsumm",  # to generate tables of functions, attributes, methods, etc.
    "sphinx_toolbox.collapse",  # support collapsable sections
    "sphinx.ext.autodoc",  # automatically generate documentation for modules
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",  # to read Google-style or Numpy-style docstrings
    "sphinxext.remoteliteralinclude",  # extends literalinclude to be able to pull files from URLs
    "sphinx.ext.viewcode",  # to allow viewing the source code in the web page
]

exclude_patterns = ["*.py"]

html_theme = "sphinx_rtd_theme"
# autodoc_inherit_docstrings = False  # don't include docstrings from the parent class
# autodoc_typehints = "description"   # Show types only in descriptions, not in signatures
