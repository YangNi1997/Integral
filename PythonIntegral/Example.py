from GaussLegendreQuadrature import *  # Gauss-Legendre Quadrature Rules in 1D, defined on [a,b]
from NewtonCotesQuadrature import *    # Newton-Cotes Closed Quadrature Rules in 1D, defined on [a,b]
from Function import *                 # integral functions

example_gausslegendre=GaussLegendreQuadrature(1,100)  # 1 and 100 are the integral bounds
result_gausslegendre=example_gausslegendre.integral(multiply_one)  # mutiply_one is the integral function
print(result_gausslegendre)


example_newtoncotes=NewtonCotesQuadrature(1,100)  # 1 and 100 are the integral bounds
result_newtoncotes=example_newtoncotes.integral(multiply_one)  # mutiply_two is the integral function
print(result_newtoncotes)
