import sys

# --- Restore a minimal working config for the test ---
project = 'ENGR 133 Teach'
copyright = '2025, Ben Manning'
author = 'Ben Manning'

extensions = [
    'jupyterbook_sphinx',
    # Keep the extension here so Sphinx tries to load it after the import test
    'jupyterlite_sphinx' 
]

source_suffix = {'.ipynb': 'jupyter_notebook', '.md': 'markdown'}
root_doc = 'intro'
html_theme = 'pydata_sphinx_theme'

html_builders = ['jupyterlite']

html_static_path = ['_static']
html_css_files = ['custom.css']

