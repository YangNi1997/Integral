#!/usr/bin/env python3
import numpy as np

class BaseQuadrature:
    def __init__(self,min,max):
        self.bound_array=np.linspace(min,max,num=10,dtype=float)
        self.abscissa_x=None
        self.weight_w=None

    def integral(self,func):
        quadrature_result=0
        for i in range(9):
            bound_min=self.bound_array[i]
            bound_max=self.bound_array[i+1]
            x_array=self.abscissa_x*(bound_max-bound_min)/2+(bound_min+bound_max)/2
            fvalue_array=func(x_array)
            quadrature=(bound_max-bound_min)/2*np.sum(self.weight_w*fvalue_array)
            quadrature_result+=quadrature
        return quadrature_result
