if(TARGET yaml-cpp::yaml-cpp AND NOT TARGET yaml-cpp)
    add_library(yaml-cpp INTERFACE IMPORTED)
    set_property(TARGET yaml-cpp PROPERTY INTERFACE_LINK_LIBRARIES yaml-cpp::yaml-cpp)
endif()
