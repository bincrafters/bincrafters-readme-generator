# -*- coding: utf-8 -*-
import os
import tempfile
import filecmp
import subprocess
import shutil


import pytest
from conans import tools
from conan_readme_generator.readme_templater import BincraftersTemplater

testdata = [
    "version-independent",
    "version-specific"
]


@pytest.mark.parametrize("readme", testdata)
def test_readme(readme):
    readme_tmpl = readme + ".md.tmpl"
    readme_expected = "expected_README_" + readme + ".md"
    temp_dir = tempfile.mkdtemp()
    with tools.chdir(os.path.join("conan_readme_generator", "test")):

        if os.path.isdir('.git'):
            shutil.rmtree('.git')
        subprocess.check_call(['git', 'init'])
        subprocess.check_call(['git', 'commit', '-m', 'test', '--allow-empty'])
        subprocess.check_call(['git', 'remote', 'add', 'origin',
                                'git@github.com:bincrafters/conan-readme-generator.git'])

        readme_templater = BincraftersTemplater()
        readme_templater.user = "foobar"
        readme_templater.channel = "testing"
        readme_templater.conan_repository = "public-conan"
        readme_templater.issue_tracker = "https://github.com/bincrafters/community/issues"
        readme_templater.prepare()
        readme_templater.run(template=os.path.join("..", "templates", "readme", readme_tmpl),
                                output=os.path.join(temp_dir, "README.md"))
        print("PATH: %s" % os.path.join(temp_dir, "README.md"))

        assert filecmp.cmp(os.path.join("file", readme_expected), os.path.join(temp_dir, "README.md"))
