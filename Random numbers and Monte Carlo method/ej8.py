from random import random

def dado():
    return int(random() * 6) + 1

gana = 0
for _ in range(1000000):
    Tirada_inicial = dado()
    
    if Tirada_inicial == 1 or Tirada_inicial == 6:

        if dado() * 2 > 6:
            gana += 1
    else:
        dado_1 = dado()
        dado_2 = dado()
        if dado_1 + dado_2 > 6:
            gana += 1

print(gana/1000000)
print(5/9)