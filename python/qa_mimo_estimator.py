#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 Matt Ettus.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from gnuradio import gr, gr_unittest
# from gnuradio import blocks
from mimo_estimator import mimo_estimator

class qa_mimo_estimator(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_instance(self):
        # FIXME: Test will fail until you pass sensible arguments to the constructor
        instance = mimo_estimator()

    def test_001_descriptive_test_name(self):
        # set up fg
        self.tb.run()
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_mimo_estimator)
