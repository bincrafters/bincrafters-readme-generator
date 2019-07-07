#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup
from setuptools import find_packages
from codecs import open
"""A simple script to generate a README.md for conan recipes.

"""
__author__ = "Bincrafters"
__license__ = "MIT"


class Version():
    '''Loads a file content'''
    __filename = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "conan_readme_generator", "__init__.py"))

    @staticmethod
    def get():
        """Retrieve package version in __init__ file

        :return:
        """
        with open(Version.__filename, "rt") as version_file:
            conan_init = version_file.read()
            version = re.search("__version__ = '([0-9a-z.-]+)'", conan_init).group(1)
            return version


class Requirements(object):
    '''Get project requirements'''

    @staticmethod
    def get(path="conan_readme_generator/requirements.txt"):
        """Retrieve all dependencies for this project

        :return:
        """
        requirements = []
        with open(path) as req_file:
            for line in req_file.read().splitlines():
                if not line.strip().startswith("#"):
                    requirements.append(line)
        return requirements


class PackageFile(object):
    '''Get configuration file list '''

    @staticmethod
    def get(directory='conan_readme_generator/templates'):
        paths = []
        for (path, directories, filenames) in os.walk(directory):
            for filename in filenames:
                paths.append(os.path.join('..', path, filename))
        return paths

setup(
    name='conan_readme_generator',
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=Version.get(),

    description='A simple script to generate a README.md for conan recipes.',

    # The project's main homepage.
    url='https://github.com/bincrafters/conan-readme-generator',

    # Author details
    author='Bincrafters',
    author_email='bicrafters@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords=['conan', 'readme', 'package', 'generator'],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=Requirements.get(),

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': Requirements.get(os.path.join('conan_readme_generator', 'requirements_test.txt'))
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        '': PackageFile.get()
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'conan-readme-generator=conan_readme_generator.main:run'
        ],
    },
)
