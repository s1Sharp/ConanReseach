from conans import ConanFile, CMake

class Test(ConanFile):
    name = "Test"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    requires = [("Quaternion/1.0")]
    generators = "cmake", "cmake_find_package"