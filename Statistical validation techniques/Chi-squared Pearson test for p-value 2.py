from random import random
from scipy.stats import chi2

esperado = [1/6,1/6,1/6,1/6,1/6,1/6]
observado = [158,172,164,181,160,165]


def estadisticoT(esperado, observado, n):
    T = 0
    for i in range(len(esperado)):
        T += (observado[i] - n * esperado[i]) ** 2 / (n * esperado[i])
    return T

T = estadisticoT(esperado, observado, n=1000)

p = 1 - chi2.cdf(T, 5)  #p-valor
print(p)

#b
def va():
    u = random()
    if u < 1/6:
        return 0
    elif u < 2/6:
        return 1
    elif u < 3/6:
        return 2
    elif u < 4/6:
        return 3
    elif u < 5/6:
        return 4
    else:
        return 5
    
def generar_muestra(size):
    muestra = [0,0,0,0,0,0]

    for _ in range(size):
        ind = va()
        muestra[ind] += 1
    return muestra

    
suma = 0
esperado = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
for i in range(1000):

    observado = generar_muestra(1000)

    T_nuevo = estadisticoT(esperado=esperado, observado=observado, n=1000)
    if T_nuevo >= T:
        suma += 1

print(suma / 1000)