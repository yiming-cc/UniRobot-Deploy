#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "genie_pb_messages::genie_pb_messages" for configuration "Release"
set_property(TARGET genie_pb_messages::genie_pb_messages APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(genie_pb_messages::genie_pb_messages PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libgenie_pb_messages.so"
  IMPORTED_SONAME_RELEASE "libgenie_pb_messages.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS genie_pb_messages::genie_pb_messages )
list(APPEND _IMPORT_CHECK_FILES_FOR_genie_pb_messages::genie_pb_messages "${_IMPORT_PREFIX}/lib/libgenie_pb_messages.so" )

# Import target "genie_pb_messages::genie_pb_messages_adapter" for configuration "Release"
set_property(TARGET genie_pb_messages::genie_pb_messages_adapter APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(genie_pb_messages::genie_pb_messages_adapter PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libgenie_pb_messages_adapter.so"
  IMPORTED_SONAME_RELEASE "libgenie_pb_messages_adapter.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS genie_pb_messages::genie_pb_messages_adapter )
list(APPEND _IMPORT_CHECK_FILES_FOR_genie_pb_messages::genie_pb_messages_adapter "${_IMPORT_PREFIX}/lib/libgenie_pb_messages_adapter.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
