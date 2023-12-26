import numpy as np
import math
import random 
from scipy.stats import norm

def rt(df): # df grados de libertad
    x = random.gauss(0.0, 1.0)
    y = 2.0*random.gammavariate(0.5*df, 2.0)
    return x / (math.sqrt(y/df))

'''def estadisticoKS(N, observaciones):
    valores = []
    est = 0
    ob = np.sort(observaciones)
    for i in range(N):
        valores.append(max((i+1)/N - norm.cdf(ob[i], 0, 1), norm.cdf(ob[i], 0, 1) - (i)/N))
    return max(valores)
'''
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

def K_S(datos):
    'Estadístico de Kolmogorov Smirnov'
    n = len(datos)
    datos.sort()
    d = 0
    for j in range(n):
        x = datos[j]
        d = max(d, (j + 1) / n - x, x - j / n)
    return d

Ns = [10, 20, 100, 10000]

for N in Ns:
    observados = [rt(11) for _ in range(N)]

    estadistico_muestra = K_S_normal(observados)
    n_sim = 100
    suma = 0

    print(estadistico_muestra)
    for i in range(n_sim):
        nueva_muestra = [random.random() for _ in range(N)]

        nuevo_est = K_S(nueva_muestra)

        if(nuevo_est > estadistico_muestra):
            suma += 1
    
    aprox_estadistico = suma / n_sim

    print(f"el p-valor para {N} datos muestrales es {aprox_estadistico}")
    



    



