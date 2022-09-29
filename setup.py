# -*- coding: utf-8 -*-

from setuptools import setup
from os import path

version = 0.1

# Load requirements
requirements = None
with open('requirements.txt') as file:
    requirements = file.read().splitlines()

# If Python3: Add "README.md" to setup.
# Useful for PyPI. Irrelevant for users using Python2.
try:
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ' '

setup(name='pythia',
      version=version,
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['pythia.timeseries','pythia.utils','pythia.effective_models'],
      package_dir = {'pythia.timeseries': 'timeseries','pythia.utils': 'utils','pythia.effective_models': 'effective_models'},
      install_requires=requirements
     )
