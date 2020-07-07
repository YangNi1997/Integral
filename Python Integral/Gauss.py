import numpy as np

class GaussLegendreQuadrature:
    def __init__(self,a_1,b_1):
        self.a=a_1
        self.b=b_1
        self.legendre_epsilon=np.array([-0.9061798459386641,-0.538469310105683,-1.081853856991421e-16,0.5384693101056831,0.9061798459386639])
        self.legendre_w=np.array([0.2369268850561892,0.4786286704993669,0.568888888888889,0.4786286704993672,0.2369268850561891])

    def callFunction(self,funcName,a):
        return funcName(a)

    def integral(self,func):
        x_array=self.legendre_epsilon*(self.b-self.a)/2+(self.a+self.b)/2
        fvalue_array=self.callFunction(func,x_array)
        quadrature=(self.b-self.a)/2*np.sum(self.legendre_w*fvalue_array)
        print(quadrature)

def func1(x):
    function=x*2
    return function

def func2(x):
    function=x*4
    return function

test1=GaussLegendreQuadrature(2,4)
test1.integral(func2)
