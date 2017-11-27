import os
import unittest
import tempfile
import filecmp
from conan_readme_generator.readme_templater import ReadmeTemplater


class GeneratorTest(unittest.TestCase):

    def test_generator(self):
        readme_templater = ReadmeTemplater()
        readme_templater.user = "foobar"
        readme_templater.channel = "testing"
        temp_dir = tempfile.mkdtemp()
        print("TEMPDIR: %s" % temp_dir)
        readme_templater.run(readme_tmpl=os.path.join("conan_readme_generator", "templates", "README.md.tmpl"), readme_out=os.path.join(temp_dir, "README.md"))
        self.assertTrue(filecmp.cmp(os.path.join("conan_readme_generator", "test", "expected_README.md"), os.path.join(temp_dir, "README.md")))
