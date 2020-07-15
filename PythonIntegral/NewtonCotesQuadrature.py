#!/usr/bin/env python3
import numpy as np
import h5py
import Function
from BaseQuadrature import BaseQuadrature

class NewtonCotesQuadrature(BaseQuadrature):
    def __init__(self,min,max):
        super().__init__(min,max)
        data=h5py.File('DataNewtonCotes.h5','r')
        newtoncotes_x=data.get('newtoncotes/abscissa_x')
        newtoncotes_w=data.get('newtoncotes/weight_w')
        self.abscissa_x=np.array(newtoncotes_x)
        self.weight_w=np.array(newtoncotes_w)
