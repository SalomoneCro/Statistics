from random import random
from scipy.stats import expon
import numpy as np
def ej4a():
    fav = 0
    for _ in range(1000):
        varal = random()
        tiempoEspera = 0
        if varal < 0.4:
            tiempoEspera = float(expon.rvs(scale=3,size=1))
        elif varal < 0.72:
            tiempoEspera = float(expon.rvs(scale=4,size=1))
        else:
            tiempoEspera = float(expon.rvs(scale=5,size=1))

        if float(tiempoEspera) < 4:
            fav += 1
    return fav / 1000

#print(ej4a())

def ej4b():
    fav = np.zeros(3)
    
    for _ in range(1000):
        varal = random()
        tiempoEspera = 0
        if varal < 0.4:
            tiempoEspera = float(expon.rvs(scale=3,size=1))
            if tiempoEspera > 4:
                fav[0] += 1
        elif varal < 0.72:
            tiempoEspera = float(expon.rvs(scale=4,size=1))
            if tiempoEspera > 4:
                fav[1] += 1
        else:
            tiempoEspera = float(expon.rvs(scale=5,size=1))
            if tiempoEspera > 4:
                fav[2] += 1

    return fav / (1 - 0.651) / 1000

print(ej4b())


