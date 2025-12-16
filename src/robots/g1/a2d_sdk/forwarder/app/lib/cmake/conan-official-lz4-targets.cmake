if(TARGET lz4::lz4 AND NOT TARGET LZ4::lz4_shared)
    add_library(LZ4::lz4_shared INTERFACE IMPORTED)
    set_property(TARGET LZ4::lz4_shared PROPERTY INTERFACE_LINK_LIBRARIES lz4::lz4)
endif()
