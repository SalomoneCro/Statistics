from random import random
def ej3(N):
    casosFav = 0
    for _ in range(N):
        ran = random()
        if ran < 1/3 :
            ranTot = random() + random()
        else:
            ranTot = random() + random() + random()
        if ranTot <= 2:
            casosFav += 1
    return casosFav / N

Ns = [100, 1000, 10000, 100000, 1000000]
for i in Ns:
    print(ej3(i))