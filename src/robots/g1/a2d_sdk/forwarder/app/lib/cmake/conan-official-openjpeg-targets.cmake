if(TARGET OpenJPEG::OpenJPEG AND NOT TARGET openjp2)
    add_library(openjp2 INTERFACE IMPORTED)
    set_property(TARGET openjp2 PROPERTY INTERFACE_LINK_LIBRARIES OpenJPEG::OpenJPEG)
endif()
