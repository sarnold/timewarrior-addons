# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version

sys.path.insert(0, os.path.abspath('../../src/timew_status'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'timew-status-indicator'
year = datetime.now().year
copyright = f"{year}, Stephen L Arnold"
author = 'Stephen L Arnold'
# The full version, including alpha/beta/rc tags
release = version('timew_addons')
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_git',
    'rst2pdf.pdfbuilder',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_sidebars = {'**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']}

source_suffix = {'.rst': 'restructuredtext'}
master_doc = "index"

description = 'Timewarrior addon bits including report extensions and a status GUI.'

# -- Options for PDF output --------------------------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# ('index', u'MyProject', u'My Project', u'Author Name',
#  dict(pdf_compressed = True))
# would mean that specific document would be compressed
# regardless of the global pdf_compressed setting.

pdf_documents = [
    #('filename', u'output filename', 'Title', 'author(s)'),
    ('index', u'timew-status-indicator', u'Timew Addons', u"Stephen L Arnold"),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['pdf']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
#pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
#pdf_language = "en_US"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
#pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
pdf_break_level = 1

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
#pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
#pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
#pdf_verbosity = 0

# If false, no index is generated.
pdf_use_index = True

# If false, no modindex is generated.
pdf_use_modindex = True

# If false, no coverpage is generated.
pdf_use_coverpage = True

# Name of the cover page template to use
#pdf_cover_template = 'sphinxcover.tmpl'

# Documents to append as an appendix to all manuals.
#pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
#pdf_splittables = False

# Set the default DPI for images
#pdf_default_dpi = 72

# Enable rst2pdf extension modules (default is empty list)
# you need vectorpdf for better sphinx's graphviz support
#pdf_extensions = ['vectorpdf']

# Page template name for "regular" pages
#pdf_page_template = 'cutePage'
