#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
import tempfile
import filecmp
import subprocess
import shutil
from conans import tools
from conan_readme_generator.readme_templater import BincraftersTemplater


class GeneratorTest(unittest.TestCase):
    def test_readme_generator(self):
        temp_dir = tempfile.mkdtemp()
        current_dir = os.getcwd()
        shutil.copyfile(
            os.path.join('conan_readme_generator', 'test', 'conanfile.py'),
            os.path.join(temp_dir, 'conanfile.py'))
        shutil.copyfile('LICENSE', os.path.join(temp_dir, 'LICENSE.md'))
        with tools.chdir(temp_dir):
            subprocess.call(['git', 'init'])
            subprocess.call([
                'git', 'remote', 'add', 'origin',
                'https://github.com/bincrafters/conan-readme-generator'
            ])
            open('.travis.yml', 'w')
            open('appveyor.yml', 'w')
            readme_templater = BincraftersTemplater()
            readme_templater.user = "foobar"
            readme_templater.channel = "testing"
            readme_templater.version = "1.0.0"
            readme_templater.name = "Hello"
            readme_templater.prepare()
            readme_templater.run(
                template=os.path.join(current_dir, "conan_readme_generator",
                                      "templates", "readme",
                                      "README-library.md.tmpl"),
                output=os.path.join("README.md"))
            self.assertTrue(
                filecmp.cmp(
                    os.path.join(current_dir, "conan_readme_generator", "test",
                                 "expected_README.md"),
                    os.path.join(temp_dir, "README.md")))
