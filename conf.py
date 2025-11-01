# conf.py

# -- Project information -----------------------------------------------------

project = 'ENGR 133 Teach'
copyright = '2025, Ben Manning'
author = 'Ben Manning'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    # Built-in extensions that Jupyter Book relies on
    'jupyterbook_sphinx',
    # The key extension for in-browser interactivity
    'jupyterlite_sphinx',
]

# The suffix(es) of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'jupyter_notebook',
    '.md': 'markdown',
}

# The root toctree document.
root_doc = 'intro' # Change 'intro' to the name of your index/landing page file (e.g., 'index')

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_book_theme'