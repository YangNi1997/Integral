#!/usr/bin/env python3
import numpy as np
import h5py
import Function
from BaseQuadrature import BaseQuadrature

class GaussLegendreQuadrature(BaseQuadrature):
    def __init__(self,min,max):
        super().__init__(min,max)
        data=h5py.File('DataLegendre.h5','r')
        legendre_x=data.get('legendre/abscissa_x')
        legendre_w=data.get('legendre/weight_w')
        self.abscissa_x=np.array(legendre_x)
        self.weight_w=np.array(legendre_w)
