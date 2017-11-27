[ ![Download](https://api.bintray.com/packages/foobar/public-conan/Hello%3Afoobar/images/download.svg) ](https://bintray.com/foobar/public-conan/Hello%3Afoobar/_latestVersion)
[![Build Status](https://travis-ci.org/foobar/conan-Hello.svg?branch=testing%2F0.1.0)](https://travis-ci.org/foobar/conan-Hello)
[![Build status](https://ci.appveyor.com/api/projects/status/sxs9n6vb8nqa92l5?svg=true)](https://ci.appveyor.com/project/foobar/conan-Hello)

[Conan.io](https://conan.io) package recipe for [Hello]().

<Description of Hello here>

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/foobar/public-conan/Hello%3Afoobar).

## For Users: Use this package

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

## For Packagers: Publish this Package

The example below shows the commands used to publish to foobar conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create foobar/testing

### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| foobar      | True |  [True, False] |
| shared      | False |  [True, False] |

## Add Remote

    $ conan remote add foobar "https://api.bintray.com/conan/foobar/public-conan"

## Upload

    $ conan upload Hello/0.1.0@foobar/testing --all -r foobar

## License
[None](LICENSE)
