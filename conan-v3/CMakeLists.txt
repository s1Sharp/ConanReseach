cmake_minimum_required(VERSION 3.9.1)
project(test)
set(PROJECT_NAME "test")

set(CMAKE_CXX_STANDARD 17)
set(GCC_COVERAGE_COMPILE_FLAGS "-Wall -pedantic -lm -O3 -funroll-loops")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GCC_COVERAGE_COMPILE_FLAGS}")

set(CMAKE_MODULE_PATH "${CMAKE_BINARY_DIR};${CMAKE_MODULE_PATH}")

# set release version
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release" CACHE STRING "Choose Release or Debug" FORCE)
endif()

# setup conan dirrectory
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
    message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
    file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/master/conan.cmake"
            "${CMAKE_BINARY_DIR}/conan.cmake")
endif()
include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_cmake_install(PATH_OR_REFERENCE ${CMAKE_SOURCE_DIR})


# set executable dirrectory
set(EXE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/executable")
set(EXECUTABLE_OUTPUT_PATH  ${EXE_DIR})

add_executable(${PROJECT_NAME} test.cpp)

find_package(Quaternion REQUIRED)
if(Quaternion_FOUND)
    message("Include target dirrectoryes")
    target_include_directories(${PROJECT_NAME} PRIVATE ${Quaternion_INCLUDE_DIRS})
    target_link_libraries(${PROJECT_NAME} PRIVATE ${Quaternion_LIBRARIES})
endif()
