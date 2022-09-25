#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 Matt Ettus.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr

class svd_precoder(gr.sync_block):
    """
    SVD Precoder, used on TX side
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="svd_precoder",
            in_sig=[numpy.complex64, ] * 6,
            out_sig=[numpy.complex64, ] * 2)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        h00 = input_items[2]
        h01 = input_items[3]
        h10 = input_items[4]
        h11 = input_items[5]
        
        out0 = output_items[0]
        out1 = output_items[1]

        for i in range(len(out0)):
            H = numpy.matrix([[h00[i],h01[i]],
                            [h10[i],h11[i]]])
            u, s, v = numpy.linalg.svd(H)

            x = numpy.matrix([[in0[i]],[in1[i]]])
            t = v.H @ x
            out0[i] = t[0]
            out1[i] = t[1]
        return len(out0)
