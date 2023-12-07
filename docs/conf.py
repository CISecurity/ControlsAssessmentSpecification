{\rtf1\ansi\ansicpg1252\cocoartf2758
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red89\green138\blue67;\red0\green0\blue0;\red193\green193\blue193;
\red140\green211\blue254;\red202\green202\blue202;\red194\green126\blue101;\red205\green173\blue106;\red70\green137\blue204;
\red196\green83\blue86;\red167\green197\blue152;}
{\*\expandedcolortbl;;\cssrgb\c41569\c60000\c33333;\csgray\c0\c0;\cssrgb\c80000\c80000\c80000;
\cssrgb\c61176\c86275\c99608;\cssrgb\c83137\c83137\c83137;\cssrgb\c80784\c56863\c47059;\cssrgb\c84314\c72941\c49020;\cssrgb\c33725\c61176\c83922;
\cssrgb\c81961\c41176\c41176;\cssrgb\c70980\c80784\c65882;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Configuration file for the Sphinx documentation builder.\cf4 \strokec4 \
\cf2 \strokec2 #\cf4 \strokec4 \
\cf2 \strokec2 # For the full list of built-in configuration values, see the documentation:\cf4 \strokec4 \
\cf2 \strokec2 # https://www.sphinx-doc.org/en/master/usage/configuration.html\cf4 \strokec4 \
\
\cf2 \strokec2 # -- Project information -----------------------------------------------------\cf4 \strokec4 \
\cf2 \strokec2 # https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information\cf4 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 project\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \cf7 \strokec7 'CIS Controls Assessment Specification'\cf4 \strokec4 \
\cf5 \strokec5 copyright\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \cf7 \strokec7 '2023, Center for Internet Security'\cf4 \strokec4 \
\cf5 \strokec5 author\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \cf7 \strokec7 'Center for Internet Security'\cf4 \strokec4 \
\cf5 \strokec5 release\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \cf7 \strokec7 '0.1'\cf4 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec2 # -- General configuration ---------------------------------------------------\cf4 \strokec4 \
\cf2 \strokec2 # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration\cf4 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 extensions\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  [\
#    \cf7 \strokec7 'sphinx.ext.imgconverter'\cf4 \strokec4 ,\
#    \cf7 \strokec7 'myst_parser'\cf4 \strokec4 ,\
    \cf7 \strokec7 'sphinx_last_updated_by_git'\cf4 \strokec4 ,\
#    \cf7 \strokec7 'sphinx.ext.intersphinx'\cf4 \strokec4 ,\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec2 #    'sphinxcontrib.video',\cf4 \strokec4 \
#    \cf7 \strokec7 'linuxdoc.rstFlatTable'\cf4 \strokec4 ,\
    \cf7 \strokec7 'sphinx.ext.viewcode'\cf4 \strokec4 ,\
\cf2 \strokec2 #    'sphinx_tabs.tabs',\cf4 \strokec4 \
\cf2 \strokec2 #    'sphinx-prompt',\cf4 \strokec4 \
#    \cf7 \strokec7 'sphinx_toolbox.collapse'\cf4 \strokec4 ,\
\cf2 \strokec2 #    'sphinx_toolbox.more_autosummary',\cf4 \strokec4 \
]\
\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 templates_path\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  [\cf7 \strokec7 '_templates'\cf4 \strokec4 ]\
\cf5 \strokec5 exclude_patterns\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  []\
\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec2 # -- Options for intersphinx -------------------------------------------------\cf4 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 #intersphinx_mapping\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \{\
#\}\
\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec2 # We recommend adding the following config value.\cf4 \strokec4 \
\cf2 \strokec2 # Sphinx defaults to automatically resolve *unresolved* labels using all your Intersphinx mappings.\cf4 \strokec4 \
\cf2 \strokec2 # This behavior has unintended side-effects, namely that documentations local references can\cf4 \strokec4 \
\cf2 \strokec2 # suddenly resolve to an external location.\cf4 \strokec4 \
\cf2 \strokec2 # See also:\cf4 \strokec4 \
\cf2 \strokec2 # https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes\cf4 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 intersphinx_disabled_reftypes\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  [\cf7 \strokec7 "*"\cf4 \strokec4 ]\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec2 # -- Options for HTML output -------------------------------------------------\cf4 \strokec4 \
\cf2 \strokec2 # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output\cf4 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 html_theme\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \cf7 \strokec7 'furo'\cf4 \strokec4 \
\cf5 \strokec5 html_static_path\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  [\cf7 \strokec7 '_static'\cf4 \strokec4 ]\
\
\cf5 \strokec5 html_short_title\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \cf7 \strokec7 'EI-ISAC Procurement Guide'\cf4 \strokec4 \
\cf5 \strokec5 html_title\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \cf7 \strokec7 'EI-ISAC\cf8 \strokec8 \\'\cf7 \strokec7 s Guide to Election Technology Procurements'\cf4 \strokec4 \
\
\cf5 \strokec5 html_theme_options\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \{\
    \cf7 \strokec7 'light_logo'\cf4 \strokec4 : \cf7 \strokec7 'EI-ISAC-Logo-Stack-2Spot-RGB.png'\cf4 \strokec4 ,\
    \cf7 \strokec7 'dark_logo'\cf4 \strokec4 : \cf7 \strokec7 'EI-ISAC-Logo-Stack-Reverse-2Spot-RGB.png'\cf4 \strokec4 ,\
    \cf7 \strokec7 "light_css_variables"\cf4 \strokec4 : \{\
        \cf7 \strokec7 "font-stack"\cf4 \strokec4 : \cf7 \strokec7 "acumin-pro, sans-serif"\cf4 \strokec4 ,\
        \cf7 \strokec7 "font-stack--monospace"\cf4 \strokec4 : \cf7 \strokec7 "Courier, monospace"\cf4 \strokec4 ,\
    \},\
\}\
\
\cf5 \strokec5 html_css_files\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  [\
    \cf7 \strokec7 'https://use.typekit.net/rcq0ndn.css'\cf4 \strokec4 ,\
]\
\
\cf5 \strokec5 html_favicon\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \cf7 \strokec7 '_static/favicon.ico'\cf4 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec2 # -- Options for MyST --------------------------------------------------------\cf4 \strokec4 \
\cf2 \strokec2 # https://myst-parser.readthedocs.io/en/stable/configuration.html\cf4 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 #latex_elements\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \{\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec2 # The paper size ('letterpaper' or 'a4paper').\cf4 \strokec4 \
#    \cf7 \strokec7 'papersize'\cf4 \strokec4 : \cf7 \strokec7 'letterpaper'\cf4 \strokec4 ,\
\
\cf2 \strokec2 # The font size ('10pt', '11pt' or '12pt').\cf4 \strokec4 \
#    \cf7 \strokec7 'pointsize'\cf4 \strokec4 : \cf7 \strokec7 '11pt'\cf4 \strokec4 ,\
\
\cf2 \strokec2 # Additional stuff for the LaTeX preamble.\cf4 \strokec4 \
#    \cf7 \strokec7 'preamble'\cf4 \strokec4 : \cf9 \strokec9 r\cf10 \strokec10 '''\cf4 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \strokec10 #        \cf8 \strokec8 \\u\cf10 \strokec10 sepackage\{charter\}\cf4 \strokec4 \
\cf10 \strokec10 #        \cf8 \strokec8 \\u\cf10 \strokec10 sepackage\cf7 \strokec7 [\cf10 \strokec10 defaultsans\cf7 \strokec7 ]\cf10 \strokec10 \{lato\}\cf4 \strokec4 \
\cf10 \strokec10 #        \cf8 \strokec8 \\u\cf10 \strokec10 sepackage\{inconsolata\}\cf4 \strokec4 \
\cf10 \strokec10 #    '''\cf4 \strokec4 ,\
#\}\
\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 myst_enable_extensions\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  [\
    \cf7 \strokec7 'colon_fence'\cf4 \strokec4 ,\
]\
\
\cf5 \strokec5 myst_heading_anchors\cf4 \strokec4  \cf6 \strokec6 =\cf4 \strokec4  \cf11 \strokec11 5\cf4 \strokec4 \
\
}
