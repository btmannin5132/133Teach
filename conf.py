import sys

# Try to import the package that should be loaded
try:
    import jupyterlite_sphinx
    #print("--- JUPYTERLITE_SPHINX WAS FOUND ---")
except ImportError:
    print("--- ERROR: JUPYTERLITE_SPHINX NOT FOUND IN THIS ENVIRONMENT ---")
    sys.exit(1) # Stop the build with an error to highlight the issue

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
html_theme = 'sphinx_book_theme'

html_builders = ['jupyterlite']