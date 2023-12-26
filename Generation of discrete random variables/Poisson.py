from random import random
from math import exp
from time import time
def Poisson(lamda):
    U = random()
    i = 0
    p = exp(-lamda)
    F = p
    while U >= F:
        i += 1
        p *= lamda / i
        F = F + p
    return i




def Poisson_m(lamda):
    p = exp(-lamda); 
    F = p
    for j in range(1, int(lamda) + 1):
        p *= lamda / j
        F += p
    U = random()
    if U >= F:
        j = int(lamda) + 1
        while U >= F:
            p *= lamda / j
            F += p
            j += 1
        return j - 1
    else:
        j = int(lamda)
        while U < F:
            F -= p
            p *= j/lamda
            j -= 1
        return j + 1


print(Poisson(5))



k = 0
z = time()
for j in range(10000):
    k += Poisson_m(100)
print(k / 10000)
print(time() - z)