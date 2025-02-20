# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os
import subprocess

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ameba Arduino AIoT Documentation'
copyright = '2024 Realtek Semiconductor Corp. All rights reserved'
author = 'REALTEK SG'
release = 'v1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx.ext.intersphinx',
    'sphinx_tabs.tabs',
    'sphinx_tags',  # Enable tagging
    'sphinx_design',
]


tags_overview_title = "Overview"
tags_page_title = 'Tag: '
tags_page_header = 'overview'
tags_create_tags = True
tags_create_badges = True
tags_badge_colors = {
    "*": "primary",
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_context = {
    "display_github": True,
    "github_user": "Ameba-AIoT",
    "github_repo": "ameba-arduino-doc",
    "github_version": "main",
    "conf_py_path": "/source/",
}

html_logo = '_static/Realtek_logo.png'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_output = '_build/html'

numfig = True

html_theme_options = {
    "collapse_navigation": False,  # Prevent tab from collapsing
    "navigation_depth": 2,  # Keep tab active
}

# Get the path to the current directory
current_dir = os.path.dirname(__file__)
# Get the path to the custom script
custom_script_path = os.path.join(current_dir, 'custom_script.py')
# Run the custom script
def run_custom_script():
    subprocess.run(['python', custom_script_path])
# Add the custom script to the build process
def setup(app):
    run_custom_script()