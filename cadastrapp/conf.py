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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# requirements
# python -m pip install gitpython
# python -m pip install sphinx
# python -m pip install sphinx_rtd_theme


import os
import re
from datetime import datetime

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year


# -- Project information -----------------------------------------------------

project = 'Cadastrapp'
copyright = str(currentYear) + ', la communauté geOrchestra'
author = 'la communauté geOrchestra'
#buildDateTime = currentDay+"/"+currentMonth+"/"+currentYear+" "+currentHour+":"+currentMinute

# The full version, including alpha/beta/rc tags
#release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

#html_theme_path = ["_themes"]

#html_theme = 'alabaster'
#html_theme = 'bizstyle'
html_theme = 'sphinx_rtd_theme'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


############################
# SETUP THE RTD LOWER-LEFT #
############################
try:
   html_context
except NameError:
   html_context = dict()
html_context['display_lower_left'] = True
 

# on lit la version courante depuis un fichier temporaire
current_version = (open("git_branch_current.txt", "r").readline())[:-1]
 
# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version


# liste des versions depuis un fichier temporaire
branch_list_file = open("git_branch_list.txt")
lines = branch_list_file.readlines()

html_context['versions'] = list()

for line in lines:
   version = line[:-1]
   if current_version != version:
      html_context['versions'].append( (version, current_version + '/') )


