
if (DEFINED Python3_VERSION_STRING)
    set(_CONAN_PYTHON_SUFFIX "3")
else()
    set(_CONAN_PYTHON_SUFFIX "")
endif()
if ("${CMAKE_CXX_COMPILER}" MATCHES "aarch64")
    set(Python${_CONAN_PYTHON_SUFFIX}_EXECUTABLE /usr/bin/python3)
else()
    set(Python${_CONAN_PYTHON_SUFFIX}_EXECUTABLE ${CMAKE_CURRENT_LIST_DIR}/../../bin/python3.10)
endif()
set(Python${_CONAN_PYTHON_SUFFIX}_LIBRARY ${CMAKE_CURRENT_LIST_DIR}/../libpython3.10.so)

# Fails if these are set beforehand
unset(Python${_CONAN_PYTHON_SUFFIX}_INCLUDE_DIRS)
unset(Python${_CONAN_PYTHON_SUFFIX}_INCLUDE_DIR)

include(${CMAKE_ROOT}/Modules/FindPython${_CONAN_PYTHON_SUFFIX}.cmake)

# Sanity check: The former comes from FindPython(3), the latter comes from the injected find module
# if(NOT Python${_CONAN_PYTHON_SUFFIX}_VERSION STREQUAL Python${_CONAN_PYTHON_SUFFIX}_VERSION_STRING)
#    message(FATAL_ERROR "CMake detected wrong cpython version - this is likely a bug with the cpython Conan package")
# endif()

if (TARGET Python${_CONAN_PYTHON_SUFFIX}::Module)
    set_target_properties(Python${_CONAN_PYTHON_SUFFIX}::Module PROPERTIES INTERFACE_LINK_LIBRARIES cpython::python)
endif()
if (TARGET Python${_CONAN_PYTHON_SUFFIX}::SABIModule)
    set_target_properties(Python${_CONAN_PYTHON_SUFFIX}::SABIModule PROPERTIES INTERFACE_LINK_LIBRARIES cpython::python)
endif()
if (TARGET Python${_CONAN_PYTHON_SUFFIX}::Python)
    set_target_properties(Python${_CONAN_PYTHON_SUFFIX}::Python PROPERTIES INTERFACE_LINK_LIBRARIES cpython::embed)
endif()
