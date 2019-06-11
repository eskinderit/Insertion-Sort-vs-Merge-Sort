import random
import math
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt

timeLimit=30
#  Insertion Sort  #
def Insertion_sort(A):
 start = timer()
 for i in range(1, len(A)):
  if timer()-start > timeLimit:
     print("Tempo Limite Superato")
     return timeLimit
  else:
     key = A[i]
     j = i-1
     while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j = j-1
     A[j+1] = key
 end = timer()
 print(end-start)
 return end-start

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
insertionSortGraph = []
mergeSortGraph = []


for j in numbervect:

  print("_____ Numeri da ordinare: ", j, "_____")
  A = random_vect(j)
  B = A.copy()

  #    Esecuzione Insertion Sort   #

  print("Tempo Insertion Sort")
  insertionSortGraph.append(Insertion_sort(A))

  #   Esecuzione Merge Sort   (timer messo fuori per comodita')  #

  start = timer()
  Merge_sort(B, 0, len(B)-1)
  end = timer()

  mergeSortGraph.append(end-start)

  print("Tempo Merge Sort ", end - start, "\n", "_____Ordinamento terminato_____", "\n")



plt.plot(numbervect,mergeSortGraph)
plt.plot(numbervect, insertionSortGraph)
plt.show()

