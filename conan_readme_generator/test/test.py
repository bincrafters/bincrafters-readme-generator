import os
import unittest
import tempfile
import filecmp
from conans import tools
from conan_readme_generator.readme_templater import ReadmeTemplater


class GeneratorTest(unittest.TestCase):

    def test_generator(self):
        temp_dir = tempfile.mkdtemp()
        with tools.chdir(os.path.join("conan_readme_generator", "test")):
            readme_templater = ReadmeTemplater()
            readme_templater.user = "foobar"
            readme_templater.channel = "testing"
            readme_templater.run(readme_tmpl=os.path.join("..", "templates", "README.md.tmpl"), readme_out=os.path.join(temp_dir, "README.md"))
            print("PATH: %s" % os.path.join(temp_dir, "README.md"))
            self.assertTrue(filecmp.cmp("expected_README.md", os.path.join(temp_dir, "README.md")))
