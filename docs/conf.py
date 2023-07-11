"""Sphinx configuration."""
project = "Wavelyt"
author = "Kinetikeith"
copyright = "2023, Kinetikeith"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
