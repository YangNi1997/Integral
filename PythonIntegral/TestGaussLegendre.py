#!/usr/bin/env python3
import unittest
import Function
from GaussLegendreQuadrature import GaussLegendreQuadrature

class TestGaussLegendre(unittest.TestCase):
    def test_function1(self):
        test1=GaussLegendreQuadrature(2,6)
        self.assertAlmostEqual((test1.bound_max*test1.bound_max-test1.bound_min*test1.bound_min)/2,test1.integral(Function.mutiply_one))

    def test_function2(self):
        test2=GaussLegendreQuadrature(1,8)
        self.assertAlmostEqual(test2.bound_max*test2.bound_max-test2.bound_min*test2.bound_min,test2.integral(Function.multiply_two))

def func1(x):
    function=x
    return function

def func2(x):
    function=x*3
    return function

if __name__=="__main__":
    unittest.main(verbosity=2)
