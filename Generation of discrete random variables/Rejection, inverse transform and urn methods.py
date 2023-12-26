from random import random

def Rech():

    c = 0.14 / 0.1 # El numerador es el mayor p_i y el denominador es el menor q_i(son todos 0.1, por ser generados por una discreta)
    ps = [0.11, 0.14, 0.09, 0.08, 0.12, 0.1, 0.09, 0.07, 0.11, 0.09]
    qs = [0.1 for _ in range(10)]

    guarda = True
    while guarda:
        u = random()
        discr_uni = int(random() * 10) + 1
        if u < (ps[discr_uni - 1] / (c * qs[discr_uni - 1])):
            guarda = False
    return discr_uni

print(Rech())


def TI():
    ps = [0.11, 0.14, 0.09, 0.08, 0.12, 0.1, 0.09, 0.07, 0.11, 0.09]
    u = random()
    if u < 0.14:
        ret = 2
    elif u < 0.14 + 0.12:
        ret = 5
    elif u < 0.14 + 0.12 + 0.11:
        ret = 1 
    elif u < 0.14 + 0.12 + 0.11 + 0.11:
        ret = 9
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1:
        ret = 6
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1 + 0.09:
        ret = 3
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1 + 2*0.09:
        ret = 7
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1 + 3*0.09:
        ret = 10
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1 + 3*0.09 + 0.08:
        ret = 4
    else:
        ret = 8
    return ret

def urna():
    valores = [0 for _ in range(100)]
    ps = [0.11, 0.14, 0.09, 0.08, 0.12, 0.1, 0.09, 0.07, 0.11, 0.09]


    i = 0
    z = 1
    for k in ps:

        for j in range(int(k * 100)):
            valores[i + j] = z
        i += int(k * 100)
        z += 1
    
    r = int(random() * 100)
    return(valores[r])

print(urna())


c = 0
q = 0
for i in range(10000):
    q = Rech()
    if q == 10:
        c += 1
print(c/10000)






