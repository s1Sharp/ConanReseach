from conans import ConanFile, CMake, tools
import os

class Quaternion(ConanFile):
    name = "Quaternion"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        print("source")
        git = tools.Git(self.source_folder)
        git.clone("https://github.com/s1Sharp/EasyQuaternion.git", branch="release_v1.0")

    def build(self):
        print("build")
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        print("package")
        self.copy("*.h", dst="inc", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        print("package_info")
        self.cpp_info.includedirs = ["inc"]
        self.cpp_info.libs = ["Quaternion"]
        self.cpp_info.libdirs = ["lib"]