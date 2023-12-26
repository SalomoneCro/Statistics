#a 
'''
def vonNeumman(x0):
    x0 = (x0 ** 2// 100) % 10000
    return x0
u = 1234
for i in range(10):
    u = vonNeumman(u)
    print(u)
'''
#b
'''
def congr(a,c,M,u):
    return((a * u + c) % M)

u = 4
for i in range(1000):
    u = congr(125,3,2**9,u)
    print(u)
'''
