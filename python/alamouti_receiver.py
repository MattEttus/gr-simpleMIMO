#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 Matt Ettus.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr

class alamouti_receiver(gr.basic_block):
    """
    docstring for block alamouti_receiver
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="alamouti_receiver",
            in_sig=[<+numpy.float32+>, ],
            out_sig=[<+numpy.float32+>, ])

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        output_items[0][:] = input_items[0]
        consume(0, len(input_items[0]))        #self.consume_each(len(input_items[0]))
        return len(output_items[0])
