import numpy as np

def Prim(Matriz_Adyacencia):
  Arbol= np.copy(Matriz_Adyacencia)
  Examinados = np.full(len(Matriz_Adyacencia), False)
  Pesos = np.full(len(Matriz_Adyacencia), np.Inf)
  Pesos[0]=0
  
  for vertice in range(len(Matriz_Adyacencia)):
    n=np.Inf
    for i in range(len(Matriz_Adyacencia)):
      print(n)
      if Pesos[i]<n and Examinados[i]==False: n=Pesos[i]
    k=np.where(Pesos==n)
    Examinados[k]=True
    for vertice_2 in  range(len(Matriz_Adyacencia)):
      if(Matriz_Adyacencia[k][vertice_2]>0 and Examinados[vertice_2]== False and Pesos[vertice_2]>Matriz_Adyacencia[k][vertice_2]):
        Pesos[vertice_2]=Matriz_Adyacencia[k][vertice_2]
  return Pesos

  print(Prim([[0,2,0,1,4,0,0],[2,0,5,0,0,0,0],[0,5,0,2,0,4,0],[1,0,2,0,0,0,0],[4,0,0,0,0,3,6],[0,0,4,0,3,0,2],[0,0,0,0,6,2,0]]))

print(np.empty(3))