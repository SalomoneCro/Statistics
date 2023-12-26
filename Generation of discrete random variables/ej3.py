from random import random

def tirada():
    return int(random() * 6) + 1

def esperanza(N):

    cont_total = 0

    for j in range(N):
        valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        ceros = [0 for _ in range(len(valores))]

        cont = 0
        while valores != ceros:
            dado1= tirada()
            dado2 = tirada()
            suma = dado1 + dado2

            for i in range(len(valores)):
                if suma == valores[i]:
                    valores[i] = 0

            cont += 1

        cont_total += cont
    return cont_total / N


def desvio(N):
    mu = esperanza(N)
    cont_total = 0
    for j in range(N):


        valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        ceros = [0 for _ in range(len(valores))]

        cont = 0
        while valores != ceros:

            dado1= tirada()
            dado2 = tirada()
            suma = dado1 + dado2

            for i in range(len(valores)):
                if suma == valores[i]:
                    valores[i] = 0

            cont += 1
        cont_total += (cont - mu) ** 2

    return (cont_total / N ) ** (1/2)
    


def estimacion(N, val):
    casos_fav = 0
    for _ in range(N):
        cont = 0
        valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        ceros = [0 for _ in range(len(valores))]


        while valores != ceros:
            dado1= tirada()
            dado2 = tirada()
            suma = dado1 + dado2

            for i in range(len(valores)):
                if suma == valores[i]:
                    valores[i] = 0

            cont += 1
        if cont <= val:
            casos_fav += 1
    return casos_fav / N



print(esperanza(1000))
print(desvio(1000))
print(1 - estimacion(1000, 14))


