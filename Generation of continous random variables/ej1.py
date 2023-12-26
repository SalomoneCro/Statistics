from random import random
from math import sqrt


def Tinversa():
    U=random()
    if U < 1/4:
        var = 2+2*sqrt(U)
    else:
        var = 6-6*sqrt(1/3 - 1/3 * U)
    return var

for _ in range(200):
    z = Tinversa()
    if int(z) != 2 and int(z)!= 5:
        print(z)
