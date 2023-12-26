from random import random
from scipy.stats import chi2

esperado = [1/4,1/2,1/4]
observado = [141,291,132]

def estadisticoT(esperado, observado, n):
    T = 0
    for i in range(len(esperado)):
        T += ((observado[i] - n * esperado[i]) ** 2) / (n * esperado[i])
    return T

T = estadisticoT(esperado=esperado, observado=observado, n=564)

p = 1 - chi2.cdf(T, 2)  #p-valor
print(p)

#b
def va():
    u = random()
    if u < 1/4:
        return 0
    elif u < 3/4:
        return 1
    else:
        return 2
    
def generar_muestra(size):
    muestra = [0,0,0]

    for _ in range(size):
        ind = va()
        muestra[ind] += 1
    return muestra

    
suma = 0
for i in range(1000):
    esperado = [1/4, 1/2, 1/4]
    observado = generar_muestra(564)

    T_nuevo = estadisticoT(esperado=esperado, observado=observado, n=564)
    if T_nuevo >= T:
        suma += 1

print(suma / 1000)

