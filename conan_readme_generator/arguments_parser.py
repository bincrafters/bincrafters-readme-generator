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
        parser = argparse.ArgumentParser(description="A simple script to generate a README.md for conan recipes.")
        
        parser.add_argument("reference", 
                            nargs='?', 
                            type=self._reference_type, 
                            default="bincrafters/stable", 
                            help='Reference to user and channel (default: "bincrafters/stable")')
                            
        parser.add_argument("template",  
                            nargs='?', 
                            type=self._path_type, 
                            default=os.path.join(pathdir, 'templates', 'README.md.tmpl'), 
                            help="Template file path (default: README.md.tmpl)")

        parser.add_argument('-d', '--debug', action='store_true', help='Switch on debug mode.')
                            
        arguments = parser.parse_args()
        self._username, self._channel = re.match(ArgumentsParser._REFERENCE_PATTERN, arguments.reference).groups()
        self._template = arguments.template
        self._debug = arguments.debug

    def _reference_type(self, string):
        if not re.match(ArgumentsParser._REFERENCE_PATTERN, string):
            raise argparse.ArgumentTypeError('Invalid reference format. See --help"')
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
    def template(self):
        return self._template

    @property
    def debug(self):
        return self._debug
