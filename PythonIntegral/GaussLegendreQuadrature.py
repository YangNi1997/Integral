#!/usr/bin/env python3
import numpy as np
import Function
from BaseQuadrature import BaseQuadrature

class GaussLegendreQuadrature(BaseQuadrature):
    def __init__(self,min,max):
        super().__init__(min,max)
        self.abscissa_x=np.array([-0.9061798459386641,-0.538469310105683,-1.081853856991421e-16,0.5384693101056831,0.9061798459386639])
        self.weight_w=np.array([0.2369268850561892,0.4786286704993669,0.568888888888889,0.4786286704993672,0.2369268850561891])
