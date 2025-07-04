# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'experthelpsolutions'
copyright = '2025, Author'
author = 'Author'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']



# -- Bing Webmaster Tools Verification Meta Tag ------------------------------

def add_bing_meta(app, pagename, templatename, context, doctree):
    context['metatags'] = context.get('metatags', '') + \
        '<meta name="msvalidate.01" content="FC509CF16E0F367160AF6AF51658C425" />\n'

def setup(app):
    app.add_config_value('meta_tags', '', 'html')
    app.connect('html-page-context', add_bing_meta)
