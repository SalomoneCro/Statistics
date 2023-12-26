from random import random
from math import log
def dis_exp(lamba):
    return -log(1-random())/lamba


for _ in range(10):

    M = dis_exp(1)
    m = dis_exp(2)
    Xis = []
    n = 10
    for _ in range(n):
        Xis.append(dis_exp(3))


    auxiliar = -1400000000
    for i in range(n):
        if Xis[i] <= M and Xis[i] > auxiliar:
            auxiliar = Xis[i]

    print(auxiliar)
    auxiliar = 1400000000

    for i in range(n):
        if Xis[i] <= m and Xis[i] < auxiliar:
            auxiliar = Xis[i]

    print(auxiliar)
    print("--------")
