# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../')) 	# Reference the root directory so autodocs can find the python modules


# -- Project information -----------------------------------------------------

project = 'HAPPy'
copyright = '2020, Mia Maric'
author = 'Mia Maric'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'nb2plots',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'HAPPY/HAPPY.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# Toc options
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
  }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'HAPPYdoc'


# -- Generate API docs during sphinx-build (for readthedocs) ------------------

# Determine if on RTD
ON_RTD = (os.environ.get('READTHEDOCS') == 'True')

def run_apidoc(_):

    from sphinx.ext import apidoc

    api_args = [
            '--force',
            '--separate',                   # Put each module on seperate page
            '--no-toc',                     # No table of contents
            '../../HAPPY',                 # Module path
            '-o',                           # Directory to output..
            '../source/HAPPY'              # here
            ]

    # Invoke apidoc
    apidoc.main(api_args)  

def setup(app):
    if ON_RTD:
        app.connect('builder-inited', run_apidoc)


# -- Extension configuration -------------------------------------------------

autodoc_member_order = 'bysource'
intersphinx_mapping = {'python': ('http://docs.python.org/3.7', None),
                       'numpy': ('http://docs.scipy.org/doc/numpy/', None),
                       'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
                       'matplotlib': ('http://matplotlib.org/', None),
                       'skimage': ('http://scikit-image.org/docs/dev/', None)}
