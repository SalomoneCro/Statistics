from random import random
from math import exp, sqrt

def i(x):
    return exp(x)/sqrt(2*x)
def ii(x):
    return (x**2)*exp(-(x**2))

valoresi = [i(random())]
valoresii = []
n = 1

def Desviacion(datos):
    suma = 0
    prom = sum(datos) / len(datos)
    for i in range(len(datos)):
        suma += (datos[i] - prom)**2
    
    return sqrt(suma / len(datos))

def integral_ab(fun, a,b,d, Nsim):
    media = fun(a + (b-a)*random()) * (b-a)
    n = 1
    scuad = 0
    while n < Nsim or sqrt(scuad/n) >= d:
        n += 1
        x = fun(a + (b-a)*random()) * (b-a)
        media_ant = media
        media = media_ant + (x - media_ant)/n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - media_ant)**2
    return media, sqrt(scuad), n


def integral_0inf(fun, d, Nsim):
    U = random()
    media = fun((1/U)-1) / U **2
    n = 1
    scuad = 0
    while n < Nsim or sqrt(scuad/n) >= d:
        n += 1
        x = fun((1/U)-1) / U **2
        media_ant = media
        media = media_ant + (x - media_ant)/n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - media_ant)**2
    return media, sqrt(scuad), n

while Desviacion(valoresi) >= 0.01 or n < 100:
    valoresi.append(i(random()))
    break


print(integral_0inf(ii, 10, 1000000))