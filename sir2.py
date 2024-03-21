import matplotlib.pyplot as plt
from pylab import *
def sir(s0, i0, r0, a, g, n, Plot = True):
    s,i,r = [s0], [i0], [r0]
    N = s0 + i0 + r0
    for j in range(n-1):
        s.append(s[j] - (a/N) * s[j] * i[j])
        i.append(i[j] + (a/N)*s[j]*i[j] - g * i[j])
        r.append(N-(s[j+1] + i[j+1]))
    if Plot:
        plt.plot(s, 'm', label = "S(n)")
        plt.plot(i, 'b', label = "I(n)")
        plt.plot(r, 'g', label = "R(n)")
        plt.legend()
        plt.xlabel('Tiempo (n)')
        plt.ylabel("Población")
        plt.title("SIR")
        plt.show()
    return (s,i,r)

param = [
    [100_000,  200_000, 0, 0.70, 0.5, 150],
    [200_000,  100_000, 0, 0.75, 0.5, 150],
    [1_000_000,10     , 0, 0.75, 0.5, 100]

]
for p in param:
    sir(p[0],p[1],p[2],p[3],p[4],p[5])
    

def sir2(s0, i0, r0, a, g, p, n, Plot = True):
    s,i,r = [s0], [i0], [r0]
    N = s0 + i0 + r0
    for j in range(n-1):
        s.append(s[j] - (a/N) * s[j] * i[j]-p*s[j])
        i.append(i[j] + (a/N)*s[j]*i[j] - g * i[j])
        r.append(N-(s[j+1] + i[j+1]))
    if Plot:
        plt.plot(s, 'm', label = "S(n)")
        plt.plot(i, 'b', label = "I(n)")
        plt.plot(r, 'g', label = "R(n)")
        plt.legend()
        plt.xlabel('Tiempo (n)')
        plt.ylabel("Población")
        plt.title("SIR")
        plt.show()
    return (s,i,r)

param2 = [
    [100_000,  200_000, 0, 0.7, 0.5, .1, 150],
    [200_000,  100_000, 0, 0.75, 0.5, .1, 150],
    [1_000_000,10     , 0, .75, 0.5, .05, 100]]
for p in param2:
    sir2(p[0], p[1], p[2], p[3], p[4], p[5], p[6])
