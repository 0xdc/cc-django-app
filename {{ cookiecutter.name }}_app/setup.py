#!/usr/bin/env python

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

base_requirements = [
    'django',
]

test_requirements = base_requirements + [
    'coverage',
]

development_requirements = test_requirements + [
    'pep8ify',
]

setup(
    name='{{ cookiecutter.name }}',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    long_description=README,
    install_requires=base_requirements,
    extras_require={
        'test': test_requirements,
        'dev': development_requirements,
    },
)
