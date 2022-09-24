#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 Matt Ettus.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr

class mimo_estimator(gr.decim_block):
    """
    docstring for block mimo_estimator
    """
    def __init__(self, alpha):
        gr.decim_block.__init__(self,
            name="mimo_estimator",
            in_sig=[numpy.complex64, numpy.complex64],
            out_sig=[numpy.complex64, numpy.complex64, numpy.complex64, numpy.complex64],
            decim=2)

        self.alpha = alpha
        self.symbol_mtx_inv = numpy.matrix( [ [ 1, 0 ], [ 0, 1 ] ]).I

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        num_proc = len(in0)//2

        for i in range(num_proc):
            H_est = numpy.matrix([[input_items[0][i*2],input_items[0][i*2+1]],
                                    [input_items[1][i*2],input_items[1][i*2+1]]])
            output_items[0][i] = input_items[0][i*2]
            output_items[1][i] = input_items[0][i*2+1]
            output_items[2][i] = input_items[1][i*2]
            output_items[3][i] = input_items[1][i*2+1]
        
        return len(output_items[0])
