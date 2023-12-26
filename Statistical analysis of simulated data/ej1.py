from random import random
from math import log, sqrt, exp

NV_MAGICCONST = 4 * exp(-0.5) / sqrt(2.0)
def Normal(mu, sigma):
    while 1:
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICCONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -log(u2):
            break
    return mu + z * sigma


def Desviacion(datos):
    suma = 0
    prom = sum(datos) / len(datos)
    for i in range(len(datos)):
        suma += (datos[i] - prom)**2
    
    return sqrt(suma / len(datos))

def gen(Nsim, d):

    media = Normal(0,1)
    n = 1
    scuad = 0
    while n < Nsim or sqrt(scuad/n) >= d:
        n += 1
        x = Normal(0,1)
        media_ant = media
        media = media_ant + (x - media_ant)/n
        scuad = scuad * (1 - 1/(n-1)) + n*(media - media_ant)**2
    return [n, media, scuad]


def Est_E(Nsim):
    p = 0
    for _ in range(Nsim):
        p += gen(100,0.1)[0]

    return p/Nsim

print(f"Se espera que n sea: {Est_E(1000)}")