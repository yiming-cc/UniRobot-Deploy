if(TARGET Freetype::Freetype AND NOT TARGET freetype)
    add_library(freetype INTERFACE IMPORTED)
    set_property(TARGET freetype PROPERTY INTERFACE_LINK_LIBRARIES Freetype::Freetype)
endif()
