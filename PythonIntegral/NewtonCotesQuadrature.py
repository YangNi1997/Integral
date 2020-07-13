#!/usr/bin/env python3
import numpy as np
import Function
from BaseQuadrature import BaseQuadrature

class NewtonCotesQuadrature(BaseQuadrature):
    def __init__(self,min,max):
        super().__init__(min,max)
        self.abscissa_x=np.array([-1.00000000000000000000,-0.50000000000000000000,0.00000000000000000000,0.50000000000000000000,1.00000000000000000000])
        self.weight_w=np.array([0.15555555555555555556,0.71111111111111111111,0.26666666666666666667,0.71111111111111111111,0.15555555555555555556])
