from random import random
from math import exp, log, e


def TI():
    return exp(random())


'''
f(x) / g(x)  con g(x) una exponencial de parametro 1     seria exp(x)/ x esta acotada por exp(e)/e en [1,e]
por lo que mi c sera igual a exp(e)/e
'''

def dis_exp(lamba):
    return -log(1-random())/lamba

def acep_rech():
    while True:
        u = random()
        Y = 1 + (e-1) * random()
        if u < 1/Y:
            return Y
        
w = 0
v = 0
n = 10000

for _ in range(n):
    w+= TI()
    v+=acep_rech()
print(v/n, w/n)
