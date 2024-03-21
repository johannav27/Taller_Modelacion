import numpy as np
import matplotlib.pyplot as plt
#Inicio de problema 2, solamente es primero obtener la nueva matriz con los pesos actualizada, después hacer 
#greedy al revés y con la trayectoria obtenida graficar
def toGraph(L):  
  x = []
  y = []
  T = Trayectoria(L)
  for i in range(len(T)):
    x.append(T[i][0])
    y.append(T[i][1]) 
  plt.plot(x,y)

def Trayectoria(L):
  j = len(L[0])
  i = len(L)
  k = 0 
  Trayectoria = [(i,j)]
  for l in range(i+j-2):
    while k != i-1 and j != 1:
      if max(L[k][j-2], L[k+1,j-1]) ==  L[k+1,j-1]:
        k += 1
      else: 
        j -= 1
      Trayectoria.append((i-k,j))
  if k == i-1 and j > 1:
    while j != 1:
      j -= 1
      Trayectoria.append((i-k,j))
  else:
    while k != i-1:
      k += 1   
      Trayectoria.append((i-k,j))
  return Trayectoria[::-1]


def matriz_con_pesos(n):          
  Pesos_O = np.ones((n,n))  
  for i in range(n):
    for j in range(n):
      Pesos_O[i][j] = np.random.exponential()
  L = np.ones((n,n)) 
  for i in range(n):
    k_1 = 0
    k_2 = 0
    for j in range(i+1):
      k_1 += Pesos_O[n-(j+1)][0]
      k_2 += Pesos_O[n-1][j]
    L[n-(i+1)][0] = k_1
    L[n-1][j] = k_2
  for i in range(1,n):
    for j in range(1,n):
      L[n-(1+i)][j] = Pesos_O[n-(1+i)][j]+max(L[n-(1+i)+1][j],L[n-(1+i)][j-1])
  return L

'''promedios = []
for j in range(3,25): 
  lista_valores_L = []
  for i in range(1000):
    lista_valores_L.append(matriz_con_pesos(j)[0][-1])
  promedio = np.mean(lista_valores_L)
  promedios.append(promedio)
  j += 1
#print(promedios)

enes = range(3, 25)
plt.scatter(enes, promedios)
m, b = np.polyfit(enes, promedios, 1)
print(m)
print(b)
plt.plot(enes, m*enes + b)
plt.show()'''


'''toGraph(matriz_con_pesos(1000))
plt.plot(range(1001), range(1001))
plt.show()

for j in range(3,50): 
  lista_valores_L = []
  lista_valores_L.append(matriz_con_pesos(j)[0][-1])'''


n=100

def g(n, alpha):
  valores = []
  for i in range(3, n):
    valor=(matriz_con_pesos(i)[0][-1]-(3.69*i-5.061))/(i**alpha)
    valores.append(valor)
  return valores

plt.plot(range(3, n), g(n, .66666))
plt.show()




