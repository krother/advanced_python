# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Advanced Python'
copyright = '2024, Kristian Rother'
author = 'Kristian Rother'
release = '1.0'
html_title = f"{project}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'myst_parser',
    ]

templates_path = ['_templates']
exclude_patterns = ['.venv', '.claude', 
                    '_build', 'Thumbs.db',
                    '.DS_Store', 'README.md']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_logo = "_static/academis_logo.png"
html_favicon = "_static/favicon.ico"

html_css_files = [
    "academis.css",
]
html_theme_options = {
    "source_repository": "https://github.com/krother/advanced_python",
    "source_branch": "master",
    "source_directory": "",
}
