
#### Requirements

Before using this Python script, you need to:

1. Install the Cheetah 3 Python Template engine:

        pip install cheetah3

2. A working conan installation:

        pip install conan
 

#### Usage

1. Copy the README.md.tmpl you would like to use into your recipe's directory, e.g. from 
    
        bincrafters-template/README.md.tmpl
   
2. Change directory into the recipe's location (i.e. where conanfile.py is)

        cd conan-libname

3. Execute this script:

        python path\to\conan_readme_templater.py 


A README.md will be generated in the `conan-libname` directory.

