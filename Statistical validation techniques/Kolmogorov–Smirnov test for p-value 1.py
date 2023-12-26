from random import random, uniform
from math import log, exp

#genero las 10 exponenciales
Y = [(-log(1 - random())) for i in range(10)]
Y.sort()

def F_exponencial(x, _lambda):
    'Distr. acumulada de la exponencial'
    return 1 - exp(-x * _lambda)


def K_S_exp(datos, theta):
    'Estadístico de Kolmogorov Smirnov'
    n = len(datos)
    datos.sort()
    d = 0
    for j in range(n):
        x = datos[j]
        d = max(d, (j+1)/n - F_exponencial(x, theta) , F_exponencial(x, theta) - j / n)
    return d

def K_S(datos):
    'Estadístico de Kolmogorov Smirnov'
    n = len(datos)
    datos.sort()
    d = 0
    for j in range(n):
        x = datos[j]
        d = max(d, (j + 1) / n - x, x - j / n)
    return d

def sim(Nsim, frec_obs, _lambda):
    d_KS = K_S_exp(frec_obs, _lambda)
    pvalor = 0
    n = len(frec_obs)
    for _ in range(Nsim):
        uniformes = []
        for _ in range(n):
            uniformes.append(uniform(0, 1))
        uniformes.sort()
        d_j= K_S(uniformes)

        if d_j >= d_KS:
            pvalor += 1
    return pvalor / Nsim

print(f"El p-valor es {sim(10000, Y,1)}")