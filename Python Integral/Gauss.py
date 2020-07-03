class Gauss_legendre_quadrature:
    def __init__(self,a_1,b_1):
        self.a=a_1
        self.b=b_1
        self.legendre_epsilon=[-0.9061798459386641,-0.538469310105683,-1.081853856991421e-16,0.5384693101056831,0.9061798459386639]
        self.legendre_w=[0.2369268850561892,0.4786286704993669,0.568888888888889,0.4786286704993672,0.2369268850561891]

    def function1(self,x):
        return x**2

    def function2(self,x,y):
        return x*y

    def function3(self,epsilon):
        x=epsilon*(self.b-self.a)/2+(self.a+self.b)/2
        return x

    def function4(self):
        quadrature=0
        value_middle=map(self.function3,self.legendre_epsilon)
        list_value_middle=list(value_middle)
        value_f=map(self.function1,list_value_middle)
        list_value_f=list(value_f)
        result=map(self.function2,list_value_f,self.legendre_w)
        list_result=list(result)

        for n in range(5):
            quadrature+=list_result[n]
        quadrature=(self.b-self.a)/2*quadrature
        print(quadrature)

test1=Gauss_legendre_quadrature(-1,3)
test1.function4()
