from random import random
from math import exp
import time

#Aproxima una sumatoria de N terminos pero con solo n calculos
def aproximacionN(N, fun, n):
    aux = 0
    for _ in range(1, n + 1):
        ran = int(random() * N) + 1
        aux += fun(ran, N)
    return aux / n * N

#a
inicio = time.time()
print(aproximacionN(10000, lambda x,y: exp(x/y), 100))
final = time.time()
print(inicio - final)
print('\n')

#b
inicio = time.time()
print(aproximacionN(10000, lambda x,y: exp(x/y), 100))
final = time.time()
print(final - inicio)
print('\n')

#c
inicio = time.time()
a = 0
for i in range(1, 10000 + 1):
    a += exp(i/10000)
print(a)
final = time.time()
print(inicio - final)
