#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Read user arguments and run Readme Templater
'''
import sys
from conan_readme_generator.readme_templater import ReadmeTemplater
from conan_readme_generator.arguments_parser import ArgumentsParser


def run():
    try:
        readme_templater = ReadmeTemplater()
    except:
        sys.exit(1)

    arguments = ArgumentsParser()
    readme_templater.user = arguments.username
    readme_templater.channel = arguments.channel
    readme_templater.run(readme_tmpl=arguments.template)

if __name__ == "__main__":
    run()
