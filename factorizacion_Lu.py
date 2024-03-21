
import numpy as np

def factorizacion_LU(matriz): #Funcion encargada de crear la matriz triangular "U"
  dim = len(matriz) #Tamaño de la matriz
  #Inicializamos dos matrices de la dimension de la matriz dada con valores ceros
  LowerMatrix = np.zeros([dim, dim])
  UpperMatrix = np.zeros([dim, dim])
  for i in range(0,dim):
    for j in range(0,dim):
      matriz[i][j] = float(matriz[i][j]) #Pasamos la matriz a matriz flotante
      UpperMatrix[i,j] = matriz[i,j]
  #Ciclo encargado de hacer operaciones para crear ceros en la matriz triangular inferior
  for p in range(0,dim):
    for i in range(0,dim):
      if (p == i): 
        LowerMatrix[p,i] = 1
      if (p < i):
        coef = (matriz[i,p]/matriz[p,p])
        LowerMatrix[i,p] = coef
        for c in range(0,dim):
          matriz[i,c] = matriz[i,c]-(coef*matriz[p,c])
          UpperMatrix[i,c] = matriz[i,c]
  return LowerMatrix, UpperMatrix #Regresa la matriz triangular con ceros debajo "U"

def DecompLU(A):
  dim = len(A) 
  LowerMatrix=np.zeros([dim, dim])
  for i in range(0,dim):
    LowerMatrix[i][i] = 1

  UpperMatrix = np.zeros([dim,dim])
  for i in range(0,dim):
    for j in range(0,dim):
      UpperMatrix[i][j] = A[i][j]

  dim = len(UpperMatrix)
  for i in range(0,dim): 
    maxElem = abs(UpperMatrix[i][i])
    maxRenglon = i
    for k in range(i+1, dim): 
      if(abs(UpperMatrix[k][i]) > maxElem):
        maxElem = abs(UpperMatrix[k][i]) 
        maxRenglon = k

    for k in range(i, dim): 
      tmp=UpperMatrix[maxRenglon][k]
      UpperMatrix[maxRenglon][k]=UpperMatrix[i][k]
      UpperMatrix[i][k]=tmp

    for k in range(i+1,dim):
      c = -UpperMatrix[k][i]/float(UpperMatrix[i][i])
      LowerMatrix[k][i] = c 
      for j in range(i, dim):
        UpperMatrix[k][j] += c*UpperMatrix[i][j] 

    for k in range(i+1, dim):
      UpperMatrix[k][i]=0
  return LowerMatrix, UpperMatrix

#print(DecompLU(np.arange(1,17).reshape(4,4)))
def resolucion_Ax_b(A, b):
  #Sustitución Ly=b, siendo Y=Ux
  LowerMatrix, UpperMatrix = factorizacion_LU(A)
  dim1 = len(LowerMatrix)
  y = np.zeros([dim1])
  for i in range(0,dim1,1):
    y[i] = b[i]/float(LowerMatrix[i][i])
    for k in range(0,i,1):
      y[i] -= y[k]*LowerMatrix[i][k]
  #Sustitución Ux=y
  dim2=len(UpperMatrix)
  x=np.zeros(dim2)
  for i in range(dim2-1,-1,-1):
    x[i] = y[i]/float(UpperMatrix[i][i])
    for k in range (i-1,-1,-1):
      UpperMatrix[i] -= x[i]*UpperMatrix[i][k]
  return x

A_ejemplo = np.array([[1,1,2],[1,-2,3],[-1,3,1]])
b_ejemplo=np.array([4,-6,7])
print(resolucion_Ax_b(A_ejemplo, b_ejemplo))
def LU(matriz):
  L=matriz
  U=[[1 if i==j else 0 for j in range(len(matriz))] for i in range(len(matriz))]
  
  for i in range(len(L)-1):
    col_zero=False
    if matriz[i][i]==0:
      col_zero=True
      for j in range(i+1,len(L)):
        if matriz[j][i]!=0:
          col_zero=False
          L[i],L[j]=L[j],L[i]
          break
    if col_zero==False:
      for j in range(i+1,len(L)):
        x=L[j][i]/L[i][i]
        for k in range(i,len(L)):
          L[j][k]=L[j][k]-(L[i][k]*x)
          U[j][k]=U[j][k]+(U[i][k]*x)
    else:
      return 0
  
  deter=1
  for i in range(len(L)):
    deter*=L[i][i]*U[i][i]
  return L, U
