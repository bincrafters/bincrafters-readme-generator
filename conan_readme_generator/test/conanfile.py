from conans import ConanFile
from conans import tools


class HelloConan(ConanFile):
    name = "Hello"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    description = "<Description of Hello here>"
    homepage = "https://github.com/bincrafters/conan-readme-generator"
    url = "None"
    license = "None"
    options = {"shared": [True, False], "foobar": [True, False]}
    default_options = "shared=False", "foobar=False"
    generators = "txt"

    def package(self):
        self.copy("*")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
