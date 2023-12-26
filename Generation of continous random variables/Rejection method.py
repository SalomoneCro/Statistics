from random import random
from math import log, e, exp
def TI(n):
    return random()**(1/n)

def Composicion(n):
    l = []
    for _ in range(n):
        l.append(random())
    return max(l)


def dis_exp(lamba):
    return -log(1-random())/lamba

def Rechazo(n):

    while True:
        Y = random()
        U = random()
        if U < (Y**(n-1)):
            return Y

uno = 0
dos = 0
tres = 0
n = 2
v = 10000
for _ in range(v):
    uno += TI(n)
    dos += Rechazo(n)
    tres += Composicion(n)

print(uno/v)
print(dos/v)
print(tres/v)
