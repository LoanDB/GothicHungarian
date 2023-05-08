# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# https://sphinx-copybutton.readthedocs.io/en/latest/index.html

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

project = 'GothicHungarian'
copyright = '2023, Viktor Martinović'
author = 'Viktor Martinović'
version = '1.0'
release = '1.0'
extensions = ['sphinx.ext.autodoc', 'sphinx_copybutton']
html_theme = 'sphinx_rtd_theme'

autodoc_mock_imports = ["loanpy", "spacy"]
