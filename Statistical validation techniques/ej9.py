from random import uniform, random
from math import exp
from math import log

frec_obs = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]
media = sum(frec_obs)/len(frec_obs)
lambd_est = 1 / media
print(f"Lambda estimado es {lambd_est}")

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

print(K_S_exp(frec_obs, lambd_est))

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

print(f"El p-valor es {sim(10000, frec_obs, lambd_est)}")

def sim_exp(Nsim, frec_obs, _lambda):

    d_KS = K_S_exp(frec_obs, _lambda)
    pvalor = 0
    n = len(frec_obs)
    lambda_est = _lambda

    for _ in range(Nsim):

        muestra_exp = []
        for _ in range(n):
            muestra_exp.append(-log(1-random())/_lambda)
        muestra_exp.sort()
        lambda_est = n/sum(muestra_exp)
        d_j= K_S_exp(muestra_exp, lambda_est)

        if d_j >= d_KS:
            pvalor += 1
    return pvalor / Nsim

print(f"Pal europa {sim_exp(10000, frec_obs, lambd_est)}")