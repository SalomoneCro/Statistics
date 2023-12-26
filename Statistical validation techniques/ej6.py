from random import random
from scipy.stats import chi2

esperado = [0.31,0.22,0.12,0.1,0.08,0.06,0.04,0.04,0.02,0.01]
observado = [188,138,87,65,48,32,30,34,13,2]
size = sum(observado)

def estadisticoT(esperado, observado, n):
    T = 0
    for i in range(len(esperado)):
        T += ((observado[i] - n * esperado[i]) ** 2) / (n * esperado[i])
    return T

#Supongo como hipotesis nula que la ruleta es honesta, quiero rechazar esta hipotesis con una confianza
# del 95%, como mi p_valor es 0.366 > alfa, con alfa = 0.05, digo que no hay suficiente evidendia para
# decir que la ruleta no es honesta.

T = estadisticoT(esperado, observado, size)
p_valor = 1 - chi2.cdf(T, 9)
print(p_valor)

def vaTeorica(lista):
    u = random()
    suma = 0
    k = 0
    for i in lista:
        suma += i
        if u < suma:
            return k
        k += 1


def generar_muestra(size):
    muestra = [0 for _ in range(10)]
    for _ in range(size):
        ind = vaTeorica(esperado)
        muestra[ind] += 1
    return muestra

suma = 0
for i in range(1000):
    observado = generar_muestra(564)

    T_nuevo = estadisticoT(esperado=esperado, observado=observado, n=564)
    if T_nuevo >= T:
        suma += 1

print(suma / 1000)
