[![Download](https://api.bintray.com/packages/foobar/public-conan/Hello%3Afoobar/images/download.svg) ](https://bintray.com/foobar/public-conan/Hello%3Afoobar/_latestVersion)

## Conan package recipe for *Hello*

<Description of Hello here>

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/foobar/public-conan/Hello%3Afoobar).


## Issues

If you wish to report an issue or make a request for a package, please do so here:

[Issue Tracker](https://github.com/bincrafters/community/issues)


## For Users

### Basic setup

    $ conan install Hello/0.1.0@foobar/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Hello/0.1.0@foobar/testing

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . foobar/testing


### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |
| foobar      | False |  [True, False] |


## Add Remote

    $ conan remote add foobar "https://api.bintray.com/conan/foobar/public-conan"


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package Hello.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](git@github.com:bincrafters/conan-readme-generator/blob/testing/0.1.0/LICENSE.md)
