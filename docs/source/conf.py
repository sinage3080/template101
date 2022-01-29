# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '파워볼커뮤니티'
copyright = '2021, Graziella'
author = '파워볼랩'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    '파워볼사이트': ('https://systemsacademy.io/', None),
    'website': ('https://systemsacademy.io/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
