# Conan Readme Generator

A simple script to generate a README.md for conan recipes.

#### Install

Before using this Python script, you need to:

1. Install all dependencies:

        pip install .

#### Usage

1. Change directory into the recipe's location (i.e. where conanfile.py is)

        cd conan-libname

2. Execute this script:

        conan-readme-generator "bincraters/channel"


A README.md will be generated in the `conan-libname` directory.

#### Testing

1. Install test requirements:

        pip install -r conan_readme_generator/requirements_test.txt

2. Execute all test:

        nosetests .

#### LICENSE
[MIT](LICENSE)
