#!/usr/bin/env python
import ez_setup
ez_setup.use_setuptools() 

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Demo Project to show how to use Allure to create BDD style tests for Python',
    'author': 'Sunitavc',
    'version': '0.1',
    'install_requires': ['nose','pip', 'nose-allure-plugin'],
    'scripts': [],
    'name': 'An Alluring Snake'
  }

setup(**config)

