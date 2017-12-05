#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Read user arguments and run Readme Templater
'''
import sys
from conan_readme_generator.readme_templater import BincraftersTemplater
from conan_readme_generator.arguments_parser import ArgumentsParser


def run():
    arguments = ArgumentsParser()

    try:
        readme_templater = BincraftersTemplater(debug=arguments.debug)
    except:
        print("An error has occured")
        sys.exit(1)

    readme_templater.user = arguments.username
    readme_templater.channel = arguments.channel
    readme_templater.prepare()

    readme_templater.run(template=arguments.readme_template)
    if readme_templater.recipe_license != 'unknown':
        readme_templater.run(template=arguments.license_template, output='LICENSE.md')


if __name__ == "__main__":
    run()
