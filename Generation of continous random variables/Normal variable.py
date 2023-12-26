from random import random
from math import log, sin, cos, pi, sqrt, exp

def Normal_rechazo(mu, sigma):
    while True:
        Y1 = -log(random())
        Y2 = -log(random())
        if Y2 >=(Y1-1) ** 2 / 2:
            if random() < 0.5:
                return Y1 * sigma + mu
            return -Y1 * sigma + mu
        
def Normal_composicion():
    z = Normal_rechazo(0,1)
    if random() < 0.5:
        return z
    else:
        return z
    
f = 0
n=10000
for _ in range(n):
    f+=Normal_composicion()
print(f/n)


def MetodoPolar(mu, sigma):
    Rcuadrado = -2 * log( 1 - random() )
    Theta= 2 * pi * random()
    X= sqrt(Rcuadrado) * cos(Theta)
    Y= sqrt(Rcuadrado) * sin(Theta)
    return (X * sigma + mu, Y * sigma + mu)

f = 0
n=10000
for _ in range(n):
    m = MetodoPolar(0,1)
    f+=m[0]
    f+=m[1]
print(f/n)

NV_MAGICCONST = 4 * exp(-0.5) / sqrt(2.0)
def normalvariate(mu, sigma):
    while 1:
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICCONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -log(u2):
            return mu + z * sigma

f = 0
n=10000
for _ in range(n):
    f+=normalvariate(10,1)
print(f/n)