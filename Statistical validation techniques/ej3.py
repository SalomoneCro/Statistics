from random import random

frec_obs = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]

def K_S(datos):
    'Estadístico de Kolmogorov Smirnov'
    n = len(datos)
    datos.sort()
    d = 0
    for j in range(n):
        x = datos[j]
        d = max(d, (j + 1) / n - x, x - j / n)
    return d

print(K_S(frec_obs))

d_KS = K_S(frec_obs) #estadıstico
pvalor = 0.
Nsim = 10000
for _ in range(Nsim):
    uniformes = []
    for _ in range(len(frec_obs)):
        uniformes.append(random())
    uniformes.sort()
    d_j= K_S(uniformes)

    if d_j >= d_KS:
        pvalor += 1
print(pvalor/Nsim)