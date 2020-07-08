import unittest
from Gauss import GaussLegendreQuadrature

class TestGauss(unittest.TestCase):
    def test_function1(self):
        test1=GaussLegendreQuadrature(2,6)
        self.assertAlmostEqual(16.0,test1.integral(func1))

    def test_function2(self):
        test2=GaussLegendreQuadrature(1,8)
        self.assertAlmostEqual(94.5,test2.integral(func2))

def func1(x):
    function=x
    return function

def func2(x):
    function=x*3
    return function

if __name__=="__main__":
    unittest.main(verbosity=2)
