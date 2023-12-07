# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ControlsAssessmentSpecification'
copyright = '2023, Center for Internet Security'
author = 'Center for Internet Security'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
#    'sphinx.ext.imgconverter',
#    'myst_parser',
    'sphinx_last_updated_by_git',
#    'sphinx.ext.intersphinx',
#    'sphinxcontrib.video',
#    'linuxdoc.rstFlatTable',
    'sphinx.ext.viewcode',
#    'sphinx_tabs.tabs',
#    'sphinx-prompt',
#    'sphinx_toolbox.collapse',
#    'sphinx_toolbox.more_autosummary',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for intersphinx -------------------------------------------------
#intersphinx_mapping = {
#}

# We recommend adding the following config value.
# Sphinx defaults to automatically resolve *unresolved* labels using all your Intersphinx mappings.
# This behavior has unintended side-effects, namely that documentations local references can
# suddenly resolve to an external location.
# See also:
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes
intersphinx_disabled_reftypes = ["*"]
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_short_title = 'EI-ISAC Procurement Guide'
html_title = 'EI-ISAC\'s Guide to Election Technology Procurements'

html_theme_options = {
    'light_logo': 'EI-ISAC-Logo-Stack-2Spot-RGB.png',
    'dark_logo': 'EI-ISAC-Logo-Stack-Reverse-2Spot-RGB.png',
    "light_css_variables": {
        "font-stack": "acumin-pro, sans-serif",
        "font-stack--monospace": "Courier, monospace",
    },
}

html_css_files = [
    'https://use.typekit.net/rcq0ndn.css',
]

html_favicon = '_static/favicon.ico'

# -- Options for MyST --------------------------------------------------------
# https://myst-parser.readthedocs.io/en/stable/configuration.html

#latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#    'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#    'pointsize': '11pt',

# Additional stuff for the LaTeX preamble.
#    'preamble': r'''
#        \usepackage{charter}
#        \usepackage[defaultsans]{lato}
#        \usepackage{inconsolata}
#    ''',
#}

myst_enable_extensions = [
    'colon_fence',
]

myst_heading_anchors = 5

