cmake_minimum_required(VERSION 3.16)
project(arduino_bridge_tests CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(PkgConfig REQUIRED)

# Ubuntu's libmsgpack-cxx-dev ships no .pc file; fall back to find_path.
if(PKG_CONFIG_FOUND)
    pkg_check_modules(MSGPACK msgpack)
    if(NOT MSGPACK_FOUND)
        pkg_check_modules(MSGPACK msgpack-cxx)
    endif()
endif()

if(NOT MSGPACK_FOUND)
    find_path(MSGPACK_INCLUDE_DIRS msgpack.hpp
        PATHS /usr/include /usr/local/include)
    if(NOT MSGPACK_INCLUDE_DIRS)
        message(FATAL_ERROR "msgpack-cxx headers not found. Install libmsgpack-dev or libmsgpack-cxx-dev.")
    endif()
    set(MSGPACK_LIBRARIES "")
endif()

add_definitions(-DMSGPACK_NO_BOOST)

add_executable(test_arduino_bridge
    tests/test_arduino_bridge.cpp
    framework-arduino-bridge/ArduinoBridgeImpl.cpp)

target_include_directories(test_arduino_bridge PRIVATE
    ${MSGPACK_INCLUDE_DIRS}
    framework-arduino-bridge)

target_link_libraries(test_arduino_bridge PRIVATE
    ${MSGPACK_LIBRARIES}
    pthread)

enable_testing()
add_test(NAME test_arduino_bridge COMMAND test_arduino_bridge)
