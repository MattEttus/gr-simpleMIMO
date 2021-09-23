#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 Matt Ettus.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr

class alamouti_estimator(gr.sync_block):
    """
    docstring for block alamouti_estimator
    """
    def __init__(self, alpha):
        gr.sync_block.__init__(self,
            name="alamouti_estimator",
            in_sig=[numpy.complex64, ],
            out_sig=[numpy.complex64, ])

        self.alpha = alpha
        self.symbol_mtx_inv = numpy.matrix( [ [ 1, 1 ], [ -1, 1 ] ]).I

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        
        num_proc = len(in0)//2

        for i in range(num_proc):            
            yb = numpy.matrix( [ [in0[i*2]], [numpy.conj(in0[i*2+1])] ] )
            H_est = self.symbol_mtx_inv * yb
            out[2*i], out[2*i+1] = H_est[0], H_est[1]
        return num_proc * 2

        
