import numpy as np

class GaussLegendreQuadrature:
    def __init__(self,a_1,b_1):
        self.a=a_1
        self.b=b_1
        self.legendre_epsilon=np.array([-0.9061798459386641,-0.538469310105683,-1.081853856991421e-16,0.5384693101056831,0.9061798459386639])
        self.legendre_w=np.array([0.2369268850561892,0.4786286704993669,0.568888888888889,0.4786286704993672,0.2369268850561891])
    def func(self,x):
        fvalue=x*2
        return fvalue

    def integral(self):
        x_array=self.legendre_epsilon*(self.b-self.a)/2+(self.a+self.b)/2
        fvalue_array=self.func(x_array)
        quadrature=(self.b-self.a)/2*np.sum(self.legendre_w*fvalue_array)
        print(quadrature)

test1=GaussLegendreQuadrature(3,6)
test1.integral()
