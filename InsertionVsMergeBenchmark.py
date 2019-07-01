import random
import math
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
import statistics
import pickle

timeLimit = 1000  # Tempo Limite

#  Insertion Sort  #


def Insertion_sort(A):
 start = timer()
 for i in range(1, len(A)):
  if timer()-start > timeLimit:
     print("ERRORE: Tempo Limite Superato")
     return timeLimit
  else:
     key = A[i]
     j = i-1
     while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j = j-1
     A[j+1] = key
 end = timer()
 return end-start

#   Merge Sort   #


def MergeSort(A, p, r):
    if p < r :
        q = (p+r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
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

#  Creo vettore random di B numeri  #


def random_vect(B):
    A=[]
    for i in range(B):
      A.append(random.randint(0, 10000)) #TODO random.seed
    return A



def MergeSortMask(A, p, r):
    start = timer()
    MergeSort(A,p,r)
    end = timer()
    return end-start


def multiple_random_vect(MultipleNumberVect, step1):
    numbervect1 = []
    for i in range(10):
        numbervect1.append(i*step1)
    for j in range(len(numbervect1)):
        MultipleNumberVect.append(random_vect(numbervect1[j]))
    return MultipleNumberVect


####################################### SIMULAZIONE #####################################



# Creazione di vettori random con passo "step"

step = 10000
numbervect = []
for i in range(10 + 1):
    numbervect.append(i*step)

insertionSortGraph = []
mergeSortGraph = []


for j in numbervect:

  print("####### Numeri da ordinare: ", j, "#######")

  RI = [] # Repeated Insertion
  RM = [] # Repeated Merge
  for z in range(1, 5):   #Indico come secondo numero il numero di volte che viene replicato l'esperimento + 1
        A = random_vect(j)
        B = A.copy()
        RI.append(Insertion_sort(A))
        RM.append(MergeSortMask(B, 0, len(B) - 1))
  I1=(statistics.mean(RI))
  I2=(statistics.mean(RM))
  print("Tempo Insertion Sort: ", I1)
  print("Tempo Merge Sort: ", I2)
  insertionSortGraph.append(I1)
  mergeSortGraph.append(I2)

#         Plot GUI

x = numbervect
y1 = mergeSortGraph
y2 = insertionSortGraph
plt.plot(numbervect, mergeSortGraph)
plt.plot(numbervect, insertionSortGraph)
plt.xlabel('Numero di elementi')
plt.ylabel('Tempo di esecuzione')
plt.title('Merge sort Vs Insertion sort Benchmark')
plt.legend(['Merge sort', 'Insertion sort'])
plt.show()


# ATTENZIONE, NON SBLOCCARE QUESTA PARTE: IL DATASET DI BASE VIENE MODIFICATO !!!
# Standard Data set to compare algs


SavedDataSet = []
multiple_random_vect(SavedDataSet, 3)

pickle_out = open("dataset.pickle", "wb")
pickle.dump(SavedDataSet, pickle_out)
pickle_out.close()

#Standard Data set read

pickle_in = open("dataset.pickle", "rb")
esempio = pickle.load(pickle_in)
print(esempio)