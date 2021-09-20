find_package(PkgConfig)

PKG_CHECK_MODULES(PC_SIMPLEMIMO simpleMIMO)

FIND_PATH(
    SIMPLEMIMO_INCLUDE_DIRS
    NAMES simpleMIMO/api.h
    HINTS $ENV{SIMPLEMIMO_DIR}/include
        ${PC_SIMPLEMIMO_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SIMPLEMIMO_LIBRARIES
    NAMES gnuradio-simpleMIMO
    HINTS $ENV{SIMPLEMIMO_DIR}/lib
        ${PC_SIMPLEMIMO_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/simpleMIMOTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SIMPLEMIMO DEFAULT_MSG SIMPLEMIMO_LIBRARIES SIMPLEMIMO_INCLUDE_DIRS)
MARK_AS_ADVANCED(SIMPLEMIMO_LIBRARIES SIMPLEMIMO_INCLUDE_DIRS)
