from random import random
from math import sqrt
from math import sin
import numpy as np
from tabulate import tabulate

def Integral_3i(fun,z_alfa_2, L): #z_alfa_2 = z_(alfa/2)
    #Confianza = (1 - alfa)%, amplitud del intervalo: L
    d = L / z_alfa_2 #sin el 2 porque dice SEMIANCHO
   
    Media = fun((np.pi)*random() + np.pi) * np.pi  #simulo X, a = pi, b = 2pi
    Scuad, n = 0, 1

    while n <= 100 or sqrt(Scuad / n) > d:
        n += 1
        #simular X
        X = fun((np.pi)*random() + np.pi) * np.pi    #a = pi, b = 2pi
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media, sqrt(Scuad), n

def fun3i(x):
    return sin(x) / x
'''
Media, s, n = Integral_3i(fun3i, 1.96, 0.001)
print(n, Media, s)
'''
def Integral_3ii(fun,z_alfa_2, L): #z_alfa_2 = z_(alfa/2)
    #Confianza = (1 - alfa)%, amplitud del intervalo: L
    d = L / (2 * z_alfa_2) #sin el 2 porque dice SEMIANCHO
    
    u = random()
    Media = fun(1/u -1) / (u**2)
    Scuad, n = 0, 1

    while n <= 100 or sqrt(Scuad / n) > d:
        n += 1
        u = random()
        X = fun(1/u -1) / (u**2)
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media, sqrt(Scuad), n


def fun3ii(x):
    return 3 / (3 + x**4)

Media, s, n = Integral_3ii(fun3ii, 1.96, 0.001)

def Tabla_3i(fun,z_alfa_2, Nsim): #z_alfa_2 = z_(alfa/2)
    #Confianza = (1 - alfa)%, amplitud del intervalo: 
   
    Media = fun((np.pi)*random() + np.pi) * np.pi  #simulo X, a=pi, b = 2pi
    Scuad, n = 0, 1

    for _ in range(Nsim):
        n += 1
        #simular X
        X = fun((np.pi)*random() + np.pi) * np.pi    #a=pi, b = 2pi
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media, sqrt(Scuad), n

def Tabla_3ii(fun,z_alfa_2, Nsim): #z_alfa_2 = z_(alfa/2)
    #Confianza = (1 - alfa)%, amplitud del intervalo: L
    
    u = random()
    Media = fun(1/u -1) / (u**2)
    Scuad, n = 0, 1

    for _ in range(Nsim):
        n += 1
        u = random()
        X = fun(1/u -1) / (u**2)
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 /(n-1)) + n*(Media - MediaAnt)**2
    return Media, sqrt(Scuad), n

primera_fila = Tabla_3ii(fun3ii, 1.96, 10000)
segunda_fila = Tabla_3ii(fun3ii, 1.96, 50000)
tercera_fila = Tabla_3ii(fun3ii, 1.96, 70000)
cuarta_fila = Tabla_3ii(fun3ii, 1.96, n)

def IC(media, z, varianza, n):
    I1 = media - (z * varianza) / sqrt(n)
    I2 = media + (z * varianza) / sqrt(n)
    return [I1, I2]


tablei = [["N sim", "I", "S", "IC(95%)"], [1000, round(primera_fila[0],4), round(primera_fila[1],4), IC(primera_fila[0], 1.96, primera_fila[1], primera_fila[2])], 
                                          [5000, round(segunda_fila[0],4), round(segunda_fila[1],4), IC(segunda_fila[0], 1.96, segunda_fila[1], segunda_fila[2])],
                                          [7000, round(tercera_fila[0],4), round(tercera_fila[1],4), IC(tercera_fila[0], 1.96, tercera_fila[1], tercera_fila[2])],
                                          [n, round(cuarta_fila[0],4), round(cuarta_fila[1],4), IC(cuarta_fila[0], 1.96, cuarta_fila[1], cuarta_fila[2])]]
print(tabulate(tablei, headers = "firstrow", tablefmt = "fancy_grid"))