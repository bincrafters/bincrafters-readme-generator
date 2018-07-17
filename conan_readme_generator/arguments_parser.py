#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import re
import os


class ArgumentsParser(object):

    _REFERENCE_PATTERN = r"(\w+)\/(\w+)"

    def __init__(self):
        path = os.path.abspath(__file__)
        pathdir = os.path.dirname(path)
        parser = argparse.ArgumentParser(
            description=
            "A simple script to generate a README.md for conan recipes.")

        parser.add_argument(
            "reference",
            nargs='?',
            type=self._reference_type,
            default="bincrafters/stable",
            help='Reference to user and channel (default: "bincrafters/stable")'
        )

        parser.add_argument(
            "readme_template",
            nargs='?',
            type=self._path_type,
            default=os.path.join(pathdir, 'templates', 'readme',
                                 'README-library.md.tmpl'),
            help=
            "README.md template file path (default: README-library.md.tmpl)")

        parser.add_argument(
            "license_template",
            nargs='?',
            type=self._path_type,
            default=os.path.join(pathdir, 'templates', 'license',
                                 'LICENSE-mit.md.tmpl'),
            help="LICENSE.md template file path (default: LICENSE-mit.md.tmpl)"
        )

        parser.add_argument(
            '-d', '--debug', action='store_true', help='Switch on debug mode.')

        arguments = parser.parse_args()
        self._username, self._channel = re.match(
            ArgumentsParser._REFERENCE_PATTERN, arguments.reference).groups()
        self._readme_template = arguments.readme_template
        self._license_template = arguments.license_template
        self._debug = arguments.debug

    def _reference_type(self, string):
        if not re.match(ArgumentsParser._REFERENCE_PATTERN, string):
            raise argparse.ArgumentTypeError(
                'Invalid reference format. See --help"')
        return string

    def _path_type(self, path):
        if not os.path.isfile(path):
            raise argparse.ArgumentTypeError('Invalid template file path')
        return path

    @property
    def username(self):
        return self._username

    @property
    def channel(self):
        return self._channel

    @property
    def readme_template(self):
        return self._readme_template

    @property
    def license_template(self):
        return self._license_template

    @property
    def debug(self):
        return self._debug
