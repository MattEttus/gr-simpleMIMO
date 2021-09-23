#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 Matt Ettus.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr

class alamouti_receiver(gr.sync_block):
    """
    docstring for block alamouti_receiver
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="alamouti_receiver",
            in_sig=[(numpy.complex64, 2) , (numpy.complex64, 8)],
            out_sig=[(numpy.complex64, 8)])


    def work(self, input_items, output_items):
        H_vec = input_items[0]
        sig = input_items[1]
        out = output_items[0]

        for i in range(sig.shape[0]):
            H_mtx = numpy.matrix( [[H_vec[i,0], H_vec[i,1]], [numpy.conj(H_vec[i,1]), -numpy.conj(H_vec[i,0])]])
            H_inv = H_mtx.I
            for j in range(4):
                x_est = numpy.matmul(H_inv, numpy.array([[sig[i,j*2]],[sig[i,j*2+1]]]))
                #x_est = numpy.matmul(H_inv, sig[i,(j*2):(j*2+2)]
                
                out[i,j*2] = x_est[0]
                out[i,j*2+1] = x_est[1]
        
        return len(output_items[0])

