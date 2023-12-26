from random import random
from numpy import random as dis
def funcion():
    u = random()
    if u < 0.5:
        return dis.exponential(3)
    elif u < 0.8:
        return dis.exponential(5)
    else:
        return dis.exponential(7)
    
sum = 0
for i in range(100000):
    sum += funcion()

print(sum / 100000)