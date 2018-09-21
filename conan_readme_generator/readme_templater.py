#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans.model.conan_file import *
from Cheetah.Template import Template
from git import Repo
import collections
import logging
import os
import re


# This class generates README.md from a template file README.md.tmpl,
class BincraftersTemplater(object):

    def __init__(self, conanfile="conanfile.py", debug=False):
        if debug:
            logging.basicConfig(level=logging.DEBUG)

        conanfile_path = os.path.join(os.getcwd(), conanfile)


        try:
            path = os.getcwd()
            while True:
                if os.path.isdir(os.path.join(path, '.git')):
                    break
                parent = os.path.dirname(path)
                if os.path.normpath(path) == os.path.normpath(parent):
                    break
                path = parent
            self.gitrepo = Repo(path)
        except Exception as e:
            if debug:
                logging.debug(e)

            print("GitPython error."
                  "\nEnsure your are executing this script in a git-controlled directory."
                  "\nMake sure the 'git' binary is available in your path.")

            raise

        self.git_active_branch = self.gitrepo.active_branch
        self.git_remote_origin_url = self.gitrepo.remotes.origin.url

        try:
            try:
                from conans.client.loader_parse import load_conanfile_class
                self.conanfile = self.loader.load_conanfile(conanfile_path)
            except ImportError:
                from conans.client.conan_api import ConanAPIV1
                conan_api, _, _ = ConanAPIV1.factory()
                self.conanfile = conan_api._loader.load_class(conanfile_path)
        except Exception as e:
            if debug:
                logging.debug(e)
            else:
                print("Could not load: %s" % conanfile_path)
            raise
        else:
            self.options = {}
            self.default_options = {}

            try:
                print("Extracting options.")
                self.options = self.parse_options(self.conanfile.options)
            except Exception as e:
                if debug:
                    logging.debug(e)
                else:
                    print("No options found in conanfile. Skipping.")
                pass
            else:
                try:
                    print("Extracting default_options.")
                    default_options = self.parse_options(self.conanfile.default_options)
                except Exception as e:
                    if debug:
                        logging.debug(e)
                    else:
                        print("No default options found in conanfile. Skipping.")
                    pass
                else:
                    for key,value in default_options.as_list():
                        self.default_options[key] = value
            finally:
                self.user = None
                self.channel = None

                self.custom_content = 'This is additional text to insert into the README.'

    def parse_options(self, opts):
        if isinstance(opts, (list, tuple)):
            return OptionsValues(opts)
        elif isinstance(opts, dict):
            return opts
        elif isinstance(opts, str):
            return OptionsValues.loads(opts)
        else:
            raise Exception("Error parsing options")

    def getConanfileVar(self, variable, default_value=''):
        if hasattr(self.conanfile, variable):
            try:
                attr = getattr(self.conanfile, variable, default_value)
            except Exception as the_exception:
                print("Failed! Debug?")
            else:
                #print("%s => %s" % (variable, type(attr)) )
                # tackles multiple or single generators definition in conanfile
                if variable == "generators":
                    if isinstance(attr, (list, tuple)):
                        return attr
                    elif isinstance(attr, str):
                        return [attr]

                if isinstance(attr, property):
                    return getattr(attr, variable, default_value)
                elif isinstance(attr, tuple):
                    return attr
                elif isinstance(attr, str):
                    return attr
                elif isinstance(attr, collections.Sequence):
                    #print("var: " + variable)
                    return attr.split()
        else:
            return default_value

    # Useful URLs:
    # https://help.github.com/articles/licensing-a-repository/
    # https://developer.github.com/v3/licenses/
    def getRecipeLicenseFromFile(self, license_file='LICENSE.md'):
        licenses_provider_URL = 'http://choosealicense.com/licenses'
        if os.path.exists(license_file):
            with open(license_file) as lic:
                lic_data = lic.read().strip()
                if "MIT License" in lic_data:
                    return { 'license': 'MIT',
                             'remote_url': '%s/%s' % (licenses_provider_URL,'mit'),
                             'url': '%s/blob/%s/%s' % (self.git_remote_origin_url,self.git_active_branch,license_file) }
                else:
                    print("Recipe License file {license_file} is not recognized.".format(license_file=license_file))
                    #return {'license': 'LICENSE',
                    #        'url': '%s/blob/%s/%s' % (self.git_remote_origin_url,self.git_active_branch,license_file) }
        else:
            print("Recipe License file {license_file} missing. Adding a default MIT license.".format(license_file=license_file))
            return {'license': 'MIT',
                    'url': '%s/blob/%s/%s' % (self.git_remote_origin_url, self.git_active_branch, license_file)}
        return {}

    def prepare(self):
        self.recipe_license = self.getRecipeLicenseFromFile()
        if not self.recipe_license:
            self.recipe_license = self.getRecipeLicenseFromFile('LICENSE')

        self.nameSpace = {'name': self.getConanfileVar('name'),
                          'version': self.getConanfileVar('version'),
                          'user': self.getConanfileVar('user', self.user),
                          'channel': self.getConanfileVar('channel', self.channel),
                          'generators': self.getConanfileVar('generators'),
                          'license': self.getConanfileVar('license'),
                          'recipe_license': self.recipe_license,
                          'homepage': self.getConanfileVar('homepage'),
                          'description': self.getConanfileVar('description'),
                          'custom_content': self.custom_content,
                          'options': self.options,
                          'default_options': self.default_options}

        for option in ('name', 'version'):
            if self.nameSpace[option] == 'None':
                print("Recipe does not have: '%s'.\nCannot produce %s" % (option, output))
                return

    def run(self, template='README.md.tmpl', output='README.md'):
        print("Generating %s using template %s" % (output,template))
        
        try:
            with open(template) as f:
                template_data = f.read()
        except Exception as ex:
            print("Could not load template: %s" % template)
        else:
            readme_parsed = Template(template_data, searchList=[self.nameSpace])

            with open(output, "w") as readme:
                readme.write(str(readme_parsed))

