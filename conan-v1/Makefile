all: conan_deps

conan_deps: conan_install quaternion

conan_install: 
	pip install conan

quaternion:
	cd conanfiles_build
	conan create .