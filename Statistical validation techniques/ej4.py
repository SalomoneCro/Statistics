import numpy as np
from random import random, uniform
from math import exp
from math import log

frec_obs = [86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99]

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

print(K_S_exp(frec_obs, 1/50))

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

print(f"El p-valor es {sim(10000, frec_obs, 1/50)}")

def sim_ii(Nsim, frec_obs):
    n = len(frec_obs)
    _lambda_est = n / sum(frec_obs)
    d_KS = K_S_exp(frec_obs, _lambda_est)
    pvalor = 0
    print(1/_lambda_est)
    for _ in range(Nsim):
        muestra = []
        for _ in range(n):
            muestra.append(-log(1 - random())/ _lambda_est)
        muestra.sort()
        _lambda_est = n / sum(muestra)
        d_j= K_S_exp(muestra, _lambda_est)

        if d_j >= d_KS:
            pvalor += 1
    return pvalor / Nsim

print(f"El p-valor es {sim_ii(10000, frec_obs)}")