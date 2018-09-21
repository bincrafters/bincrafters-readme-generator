import os
import unittest
import tempfile
import filecmp
from conans import tools
from conan_readme_generator.readme_templater import BincraftersTemplater


class GeneratorTest(unittest.TestCase):

    def test_generator(self):
        temp_dir = tempfile.mkdtemp()
        with tools.chdir(os.path.join("conan_readme_generator", "test")):
            readme_templater = BincraftersTemplater()
            readme_templater.user = "foobar"
            readme_templater.channel = "testing"
            readme_templater.prepare()
            readme_templater.run(template=os.path.join("..", "templates", "readme", "README-library.md.tmpl"),
                                 output=os.path.join(temp_dir, "README.md"))
            print("PATH: %s" % os.path.join(temp_dir, "README.md"))
            self.assertTrue(filecmp.cmp("expected_README.md", os.path.join(temp_dir, "README.md")))
