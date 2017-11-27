#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

#### Requirements

Before using this Python script, you need to:

1. Install the Cheetah 3 Python Template engine:

        pip install cheetah3

2. A working conan installation:

        pip install conan


#### Usage

1. Copy the README.md.tmpl you would like to use into your recipe's directory, e.g. from

        bincrafters-template/README.md.tmpl

2. Change directory into the recipe's location (i.e. where conanfile.py is)

        cd conan-libname

3. Execute this script:

        python path\to\conan_readme_templater.py


A README.md will be generated in the `conan-libname` directory.

'''


from Cheetah.Template import Template
from conans.client.loader_parse import load_conanfile_class
import os

# This class generates README.md from a template file README.md.tmpl,
class ReadmeTemplater(object):

    def __init__(self):
        conanfile_path = os.path.join(os.getcwd(), "conanfile.py")
        self.conanfile = load_conanfile_class(conanfile_path)

        self.options = self.conanfile.options
        self.default_options = {}

        default_options = self.conanfile.default_options
        for dopt in default_options:
            key, value = dopt.split("=")
            self.default_options[key] = value

        self.user = None
        self.channel = None

        self.custom_content = 'This is additional text to insert into the README.'

    def getConanfileVar(self, variable, default_value=''):
        if hasattr(self.conanfile, variable):
            try:
                attr = getattr(self.conanfile, variable, default_value)
            except Exception as the_exception:
                print("Failed! Debug?")
            else:
                if not isinstance(attr, property):
                    return '{0}'.format(str(attr))
                else:
                    return getattr(attr, variable, default_value)
        else:
            return default_value

    def run(self, readme_tmpl='README.md.tmpl', readme_out='README.md'):

        self.nameSpace = {'name': self.getConanfileVar('name'),
                          'version': self.getConanfileVar('version'),
                          'user': self.getConanfileVar('user', self.user),
                          'channel': self.getConanfileVar('channel', self.channel),
                          'license': self.getConanfileVar('license'),
                          'homepage': self.getConanfileVar('homepage'),
                          'description': self.getConanfileVar('description'),
                          'custom_content': self.custom_content,
                          'options': self.options,
                          'default_options': self.default_options}

        with open(readme_tmpl) as f:
            template_data = f.read()

        readme_parsed = Template(template_data, searchList=[self.nameSpace])

        with open(readme_out, "w") as readme:
            readme.write(str(readme_parsed))
