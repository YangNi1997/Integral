#!/usr/bin/env python3
import numpy as np

class BaseQuadrature:
    def __init__(self,min,max):
        self.bound_min=min
        self.bound_max=max
        self.legendre_x=None
        self.legendre_w=None

    def integral(self,func):
        x_array=self.legendre_x*(self.bound_max-self.bound_min)/2+(self.bound_min+self.bound_max)/2
        fvalue_array=func(x_array)
        quadrature=(self.bound_max-self.bound_min)/2*np.sum(self.legendre_w*fvalue_array)
        print(quadrature)
        return quadrature
