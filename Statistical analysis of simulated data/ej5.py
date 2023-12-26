from random import random
from math import sqrt

def M():
    u1 = random()
    u2 = random()
    n = 2
    while u1 <= u2:
        u1 = u2
        u2 = random()
        n += 1
    return n

def simulacion_e(L): #z_alfa_2 = z_(alfa/2)
    n = 1 
    mediaN = M()
    Scuad = 1

    while Scuad/n > L:
        n += 1
        X = M()
        media_ant = mediaN
        mediaN = media_ant + (X - media_ant)/n
        Scuad = Scuad * (1 - 1/(n-1)) + n*(mediaN - media_ant)**2
    
    return n, mediaN, Scuad

muestra = simulacion_e(0.01)
n = muestra[0]
mediaN = muestra[1]
scuad = muestra[2]

print(f"La estimación de e es {mediaN}")
print(f"La varianza muestral es de {scuad}")

def e_estimation(dessired_width, z_alfa_2):

    n = 1
    vari = 1
    mean = M()

    while 2 * z_alfa_2 * sqrt(vari/n) > dessired_width:
        n += 1
        X = M()
        old_mean = mean
        mean = old_mean + (X - old_mean) / n
        vari = vari * (1 - 1 / (n - 1)) + n*(mean - old_mean)**2
    return mean, n

print(e_estimation(0.001, 2.33))