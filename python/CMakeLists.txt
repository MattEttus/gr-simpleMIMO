# Copyright 2011 Free Software Foundation, Inc.
#
# This file was generated by gr_modtool, a tool from the GNU Radio framework
# This file is a part of gr-simpleMIMO
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Include python install macros
########################################################################
include(GrPython)
if(NOT PYTHONINTERP_FOUND)
    return()
endif()

add_subdirectory(bindings)

########################################################################
# Install python sources
########################################################################
GR_PYTHON_INSTALL(
    FILES
    __init__.py
    alamouti_estimator.py
    alamouti_receiver.py
    mimo_estimator.py
    svd_precoder.py
    svd_postcoder.py DESTINATION ${GR_PYTHON_DIR}/simpleMIMO
)

########################################################################
# Handle the unit tests
########################################################################
include(GrTest)

set(GR_TEST_TARGET_DEPS gnuradio-simpleMIMO)
GR_ADD_TEST(qa_alamouti_estimator ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_alamouti_estimator.py)
GR_ADD_TEST(qa_alamouti_receiver ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_alamouti_receiver.py)
GR_ADD_TEST(qa_mimo_estimator ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_mimo_estimator.py)
GR_ADD_TEST(qa_svd_precoder ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_svd_precoder.py)
GR_ADD_TEST(qa_svd_postcoder ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_svd_postcoder.py)
