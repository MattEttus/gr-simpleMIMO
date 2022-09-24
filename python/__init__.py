#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

# The presence of this file turns this directory into a Python package

'''
This is the GNU Radio SIMPLEMIMO module. Place your Python package
description here (python/__init__.py).
'''
import os

# import pybind11 generated symbols into the simpleMIMO namespace
try:
    # this might fail if the module is python-only
    from .simpleMIMO_python import *
except ModuleNotFoundError:
    pass

# import any pure python here
from .alamouti_estimator import alamouti_estimator
from .alamouti_receiver import alamouti_receiver
from .mimo_estimator import mimo_estimator
from .svd_precoder import svd_precoder
from .svd_postcoder import svd_postcoder

#
