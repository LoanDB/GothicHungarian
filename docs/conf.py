# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'GothicHungarian'
copyright = '2023, Viktor Martinović'
author = 'Viktor Martinović'
version = '1.0'
release = '1.0'
extensions = ['sphinx.ext.autodoc']
html_theme = 'sphinx_rtd_theme'
# TODO replace mock with docs/requirements.txt after loanpy-release
autodoc_mock_imports = ["loanpy.loanfinder", "spacy"]
