# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'overcooked-ebiomedpku'
copyright = '2026, Computational Biomedicine Lab, Peking University'
author = 'Computational Biomedicine Lab'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx.ext.autodoc", "sphinx.ext.viewcode"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ['_templates']
exclude_patterns = []

myst_enable_extensions = [
    "colon_fence",      # 使用:::语法创建代码块
    "deflist",          # 支持定义列表
    "dollarmath",       # 支持LaTeX数学公式
    "linkify",          # 自动识别URL链接
    "substitution",     # 支持变量替换
    "tasklist",         # 支持任务列表
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_static_path = ['_static']