from random import random
from math import exp, cos
def g(u): ##funcion a integrar en (0,1) ´
    return (1 - u ** 2) ** (1.5)

##estimacion de la integral de g con Nsim simulaciones (entre 0 y 1)
def MonteCarlo(funciong, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += funciong(random())
    return Integral/Nsim    

##Estima la integral de funciong entre a y b con Nsim simulaciones (entre a y b)
def IntegralMonteCarlo(funciong, a, b, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += funciong(a + (b-a) * random())
    return Integral * (b-a)/Nsim

#Integral entre 0 e infinito
def MonteCarloinf(funciong, Nsim):
    Integral = 0
    for _ in range(Nsim):
        y = random()
        Integral += (1 / y**2) * funciong(1 / y - 1)
    return Integral / Nsim

print(MonteCarloinf(lambda x: exp((-(x**2))), 1000000) * 2)