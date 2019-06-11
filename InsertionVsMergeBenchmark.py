import random
import math
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

#  Insertion Sort  #

def Insertion_sort(A):
 start = timer()
 for i in range(1, len(A)):
  if timer()-start > 300:
     return print("Tempo Insertion Sort: Il tempo supera i 5 min")
  else:
     key = A[i]
     j = i-1
     while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j = j-1
     A[j+1] = key
 end = timer()
 return print("Tempo Insertion Sort", end-start)

#   Merge Sort   #

def Merge_sort(A, p, r):
    if p < r :
        q = (p+r) // 2
        Merge_sort(A, p, q)
        Merge_sort(A, q+1, r)
        Merge(A, p, q, r)

def Merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[]
    R=[]
    for i in range (0,n1):
        L.append(A[p+i])
    for j in range (0,n2):
        R.append(A[q+j+1])
    L.append(math.inf)
    R.append(math.inf)
    i=0
    j=0
    for k in range (p,r +1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

#  Creo vettori random di numeri  #
def random_vect(B):
    A=[]
    for i in range(B):
      A.append(random.randint(-100,100))
    return A

#          dimensione del vettore dei numeri da ordinare

numbervect = [10,100,1000,10000,100000,1000000]



for j in numbervect:

  print("_____ Numeri da ordinare: ", j, "_____")
  A = random_vect(j)
  B = A.copy()

  #    Esecuzione Insertion Sort   #

  Insertion_sort(A)

  #    Esecuzione Merge Sort   (timer messo fuori per comodita')  #

  start = timer()
  Merge_sort(B, 0, len(B)-1)
  end = timer()
  print("Tempo Merge Sort ", end - start, "\n", "_____Ordinamento terminato_____", "\n")

  # Plot

x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()