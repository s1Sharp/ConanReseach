from conans import ConanFile, CMake, tools
import os

class Quaternion(ConanFile):
    name = "Quaternion"
    # version - get while build
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        print("clone")
        src_dir = os.path.join(self.source_folder, "src")
        git = tools.Git(src_dir)
        git.clone("https://github.com/s1Sharp/EasyQuaternion.git")

        print("checkout")
        commit = self.conan_data["versions"][self.version]
        git.checkout(commit)

    def build(self):
        print("build")
        src_dir = os.path.join(self.source_folder, "src")
        cmake = CMake(self)

        cmake.configure(source_folder=src_dir)
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