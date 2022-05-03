all: conan_deps run

build: cmake
cmake: 
	cmake --build build/ --config Release --target test -j 6
run: build
	./executable/*/test.exe


conan_deps: conan_install quaternion
conan_install: 
	pip install conan
quaternion:
	conan create ./conanfiles_build