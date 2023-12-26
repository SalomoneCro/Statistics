from random import uniform, random
from scipy.stats import norm
import math

frec_obs = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]
mu = sum(frec_obs)/len(frec_obs)
sigma = (sum((frec_obs[i] - mu)**2 for i in range(len(frec_obs))) / (len(frec_obs) - 1)) ** 0.5
print(f"Media: {mu}")
print(f"Varinaza: {sigma}")



#Normalizo los datos
datos = [(frec_obs[i]-mu)/sigma for i in range(len(frec_obs))]

mu = sum(datos)/len(frec_obs)
sigma = (sum((datos[i] - mu)**2 for i in range(len(frec_obs))) / (len(frec_obs) - 1)) ** 0.5
print(f"Media: {mu}")
print(f"Varinaza: {sigma}")


def K_S(datos):
    'Estadístico de Kolmogorov Smirnov'
    n = len(datos)
    datos.sort()
    d = 0
    for j in range(n):
        x = datos[j]
        d = max(d, (j + 1) / n - x, x - j / n)
    return d

def K_S_normal(datos):
    'Estadístico de Kolmogorov Smirnov para X ∼ N(mu, sigma)'
    n = len(datos)
    datos.sort()
    d = 0
    for j in range(n):
        x = datos[j]
        p = math.erf(x/math.sqrt(2))/2 + 0.5
        d = max(d, (j + 1) / n - p, p - j / n)
    return d

print(K_S_normal(datos))

def sim(Nsim, frec_obs, mu, sigma):
    d_KS = K_S_normal(frec_obs)
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

print(f"El p-valor es {sim(10000, frec_obs, mu, sigma)}")


from math import exp, sqrt, log 
NV_MAGICCONST = 4 * exp(-0.5) / sqrt(2.0)

def normalvariate(mu, sigma):
    while 1:
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICCONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -log(u2):
            break
    return mu + z * sigma

def sim2(Nsim, frec_obs, mu, sigma):

    d_KS = K_S_normal(frec_obs)
    pvalor = 0
    n = len(frec_obs)

    for _ in range(Nsim):

        uniformes = []
        for _ in range(n):
            uniformes.append(normalvariate(mu, sigma))
        uniformes.sort()

        d_j= K_S_normal(uniformes)

        if d_j >= d_KS:
            pvalor += 1
    return pvalor / Nsim

print(f"El p-valor es {sim2(10000, frec_obs, mu, sigma)}")