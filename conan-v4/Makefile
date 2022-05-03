all: conan_deps build

build: cmake
cmake: 
	cmake --build build/ --config Release --target test -j 6 | echo "expected error cmake build"


conan_deps: conan_install quaternion
conan_install: 
	pip install conan
quaternion:
	conan create ./conanfiles_build Quaternion/1.0@pr/pr -pr win