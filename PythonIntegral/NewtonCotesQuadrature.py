#!/usr/bin/env python3
import numpy as np
from BaseQuadrature import BaseQuadrature

class NewtonCotesQuadrature(BaseQuadrature):
    def __init__(self,a_1,b_1):
        super().__init__(a_1,b_1)
        self.legendre_epsilon=np.array([-1.00000000000000000000,-0.50000000000000000000,0.00000000000000000000,0.50000000000000000000,1.00000000000000000000])
        self.legendre_w=np.array([0.15555555555555555556,0.71111111111111111111,0.26666666666666666667,0.71111111111111111111,0.15555555555555555556])

def func1(x):
    function=x
    return function

def func2(x):
    function=x*4
    return function

test2=NewtonCotesQuadrature(2,8)
test2.integral(func1)
