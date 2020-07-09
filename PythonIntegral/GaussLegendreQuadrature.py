#!/usr/bin/env python3
import numpy as np
from BaseQuadrature import BaseQuadrature

class GaussLegendreQuadrature(BaseQuadrature):
    def __init__(self,a_1,b_1):
        super().__init__(a_1,b_1)
        self.legendre_epsilon=np.array([-0.9061798459386641,-0.538469310105683,-1.081853856991421e-16,0.5384693101056831,0.9061798459386639])
        self.legendre_w=np.array([0.2369268850561892,0.4786286704993669,0.568888888888889,0.4786286704993672,0.2369268850561891])

def func1(x):
    function=x*2
    return function

def func2(x):
    function=x
    return function

test1=GaussLegendreQuadrature(1,8)
test1.integral(func2)
