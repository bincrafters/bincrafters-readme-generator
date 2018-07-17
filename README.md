# Conan Readme Generator

A simple script to generate a README.md for conan recipes.

![logo](logo.png)

#### Install

Before using this Python script, you need to:

1. Install the script and all its dependencies. There are two ways:

       a) pip install git+https://github.com/bincrafters/conan-readme-generator --upgrade

        or

       b) git clone https://github.com/bincrafters/conan-readme-generator
          cd conan-readme-generator
          pip install . --upgrade

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
