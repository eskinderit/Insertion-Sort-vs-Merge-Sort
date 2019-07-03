import random
import math
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
import statistics
import pickle

timeLimit = 1000  # Tempo Limite 16.6 minuti

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


def incr_vect(B):
    A=[]
    for i in range(B+1):
        A.append(i)
    return A


def decr_vect(B):
    A=[]
    for i in range(B,-1,-1):
        A.append(i)
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

#Standard Data set read



def testComparison(rep,Setfile):  #indico il numero di ripetizioni ed il file sorgente
 insertionSortGraph=[]
 mergeSortGraph=[]
 print("INIZIO TEST DI CONFRONTO: ", Setfile)
 pickle_in = open(Setfile, "rb")
 Set = pickle.load(pickle_in)
 for j in range(0, len(Set)):
     print("Passo: ",j+1,"/", len(Set), " Elementi: ",len(Set[j]))
     IS = []
     MS = []
     for i in range(0, rep + 1):  # numero di ripetizioni
        Set = []
        pickle_in = open(Setfile, "rb")
        Set = pickle.load(pickle_in)
        SetCopy = Set.copy()
        IS.append(Insertion_sort(Set[j]))
        MS.append(MergeSortMask(SetCopy[j], 0, len(SetCopy[j])-1))
     ISAverage = (statistics.mean(IS))
     MSAverage = (statistics.mean(MS))
     print("Il tempo impiegato da Insertion Sort e' :", ISAverage)
     print("Il tempo impiegato da Merge Sort e': ", MSAverage)
     insertionSortGraph.append(ISAverage)
     mergeSortGraph.append(MSAverage)

 # PLOT
 Set = []
 ElementsNum=[]
 pickle_in = open(Setfile, "rb")
 Set = pickle.load(pickle_in)
 for z in range(0,len(Set)):
     A=Set[z]
     print(A)
     ElementsNum.append(len(A))
 plt.plot(ElementsNum, mergeSortGraph)
 plt.plot(ElementsNum, insertionSortGraph)
 plt.xlabel('Numero di elementi')
 plt.ylabel('Tempo di esecuzione')
 plt.title('Merge sort Vs Insertion sort Benchmark')
 plt.legend(['Merge sort', 'Insertion sort'])
 plt.show()

# insertion sort best case


testComparison(4, "incrBigDataset.pickle")
testComparison(900, "incrSmallDataset.pickle")


# insertion sort worst case


testComparison(4, "decrBigDataset.pickle")
testComparison(900, "decrSmallDataset.pickle")

# average case

testComparison(4, "randomBigDataset.pickle")
testComparison(900, "randomSmallDataset.pickle")

#da rifare 1,2,5 ma soprattutto 6