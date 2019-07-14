import random
import math
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import statistics
import pickle

# SET TIME LIMIT HERE

timeLimit = 1000  # Limits Time 16.6 mins

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

#   Merge   #

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

#  Creates random vector of B int nums  #

def random_vect(B):
    A=[]
    for i in range(B):
      A.append(random.randint(0, 10000)) #TODO random.seed
    return A

# Creates (increasing) order vect of B int nums  #

def incr_vect(B):
    A=[]
    for i in range(B+1):
        A.append(i)
    return A

# Creates (decreasing) order vect of B int nums #

def decr_vect(B):
    A=[]
    for i in range(B,-1,-1):
        A.append(i)
    return A

# Merge sort with mask that returns timer #

def MergeSortMask(A, p, r):
    start = timer()
    MergeSort(A,p,r)
    end = timer()
    return end-start

# Creates an array of arrays made of random numbers. MultipleNumbersVect MUST be empty

def multiple_random_vect(MultipleNumberVect, step1):
    numbervect1 = []
    for i in range(10):
        numbervect1.append(i*step1)
    for j in range(len(numbervect1)):
        MultipleNumberVect.append(random_vect(numbervect1[j]))
    return MultipleNumberVect

# Merge vs Insertion comparison with the data set you want to use

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
     ElementsNum.append(len(A))
 plt.plot(ElementsNum, mergeSortGraph,'--bo')
 plt.plot(ElementsNum, insertionSortGraph, '--ro')
 plt.xlabel('Numero di elementi')
 plt.ylabel('Tempo di esecuzione')
 plt.title('Merge sort Vs Insertion sort Benchmark')
 plt.legend(['Merge sort', 'Insertion sort'])
 plt.grid(True)
 plt.xticks(ElementsNum)
 plt.xticks(rotation=45)
 plt.show()

# tests merge sort with datasets defined inside

def mergeTestComparison(rep):  # indico il numero di ripetizioni ed il file sorgente
     Setfile1="randomBigDataset.pickle"
     Setfile2="incrBigDataset.pickle"
     Setfile3="decrBigDataset.pickle"
     mergeSortGraph1 = []
     mergeSortGraph2 = []
     mergeSortGraph3 = []
     print("INIZIO TEST DI CONFRONTO: ", Setfile1)
     pickle_in = open(Setfile1, "rb")
     Set = pickle.load(pickle_in)
     for j in range(0, len(Set)):
         print("Passo: ", j + 1, "/", len(Set), " Elementi: ", len(Set[j]))
         MS = []
         for i in range(0, rep + 1):  # numero di ripetizioni
             Set = []
             pickle_in = open(Setfile1, "rb")
             Set = pickle.load(pickle_in)
             SetCopy = Set.copy()
             MS.append(MergeSortMask(SetCopy[j], 0, len(SetCopy[j]) - 1))
         MSAverage = (statistics.mean(MS))
         print("Il tempo impiegato da Merge Sort (input random) e': ", MSAverage)
         mergeSortGraph1.append(MSAverage)

     print("INIZIO TEST DI CONFRONTO: ", Setfile2)
     pickle_in = open(Setfile2, "rb")
     Set = pickle.load(pickle_in)
     for j in range(0, len(Set)):
         print("Passo: ", j + 1, "/", len(Set), " Elementi: ", len(Set[j]))
         MS = []
         for i in range(0, rep + 1):  # numero di ripetizioni
             Set = []
             pickle_in = open(Setfile2, "rb")
             Set = pickle.load(pickle_in)
             SetCopy = Set.copy()
             MS.append(MergeSortMask(SetCopy[j], 0, len(SetCopy[j]) - 1))
         MSAverage = (statistics.mean(MS))
         print("Il tempo impiegato da Merge Sort (input incr) e': ", MSAverage)
         mergeSortGraph2.append(MSAverage)

     print("INIZIO TEST DI CONFRONTO: ", Setfile3)
     pickle_in = open(Setfile3, "rb")
     Set = pickle.load(pickle_in)
     for j in range(0, len(Set)):
         print("Passo: ", j + 1, "/", len(Set), " Elementi: ", len(Set[j]))
         MS = []
         for i in range(0, rep + 1):  # numero di ripetizioni
             Set = []
             pickle_in = open(Setfile3, "rb")
             Set = pickle.load(pickle_in)
             SetCopy = Set.copy()
             MS.append(MergeSortMask(SetCopy[j], 0, len(SetCopy[j]) - 1))
         MSAverage = (statistics.mean(MS))
         print("Il tempo impiegato da Merge Sort (input decr) e': ", MSAverage)
         mergeSortGraph3.append(MSAverage)

     # PLOT

     Set = []
     ElementsNum = []
     pickle_in = open(Setfile1, "rb")
     Set = pickle.load(pickle_in)
     for z in range(0, len(Set)):
         A = Set[z]
         ElementsNum.append(len(A))
     plt.plot(ElementsNum, mergeSortGraph1, '--bo')
     plt.plot(ElementsNum, mergeSortGraph2, '--ro')
     plt.plot(ElementsNum, mergeSortGraph3, '--go')
     plt.xlabel('Numero di elementi')
     plt.ylabel('Tempo di esecuzione')
     plt.title('I casi di merge sort')
     plt.legend(['Input random', 'Input in ord. crescente', 'Input in ord. decr'])
     plt.grid(True)
     plt.xticks(ElementsNum)
     plt.xticks(rotation=45)

     plt.show()

# test insertion sort with datasets defined inside

def insertionTestComparison(rep):  # indico il numero di ripetizioni ed il file sorgente
     Setfile1="randomBigDataset.pickle"
     Setfile2="incrBigDataset.pickle"
     Setfile3="decrBigDataset.pickle"
     insertionSortGraph1 = []
     insertionSortGraph2 = []
     insertionSortGraph3 = []
     print("INIZIO TEST DI CONFRONTO: ", Setfile1)
     pickle_in = open(Setfile1, "rb")
     Set = pickle.load(pickle_in)
     for j in range(0, len(Set)):
         print("Passo: ", j + 1, "/", len(Set), " Elementi: ", len(Set[j]))
         IS = []
         for i in range(0, rep + 1):  # numero di ripetizioni
             Set = []
             pickle_in = open(Setfile1, "rb")
             Set = pickle.load(pickle_in)
             SetCopy = Set.copy()
             IS.append(Insertion_sort(Set[j]))
         ISAverage = (statistics.mean(IS))
         print("Il tempo impiegato da Insertion Sort (input random) e': ", ISAverage)
         insertionSortGraph1.append(ISAverage)

     print("INIZIO TEST DI CONFRONTO: ", Setfile2)
     pickle_in = open(Setfile2, "rb")
     Set = pickle.load(pickle_in)
     for j in range(0, len(Set)):
         print("Passo: ", j + 1, "/", len(Set), " Elementi: ", len(Set[j]))
         IS = []
         for i in range(0, rep + 1):  # numero di ripetizioni
             Set = []
             pickle_in = open(Setfile2, "rb")
             Set = pickle.load(pickle_in)
             SetCopy = Set.copy()
             IS.append(Insertion_sort(Set[j]))
         ISAverage = (statistics.mean(IS))
         print("Il tempo impiegato da Insertion Sort (input incr) e': ", ISAverage)
         insertionSortGraph2.append(ISAverage)

     print("INIZIO TEST DI CONFRONTO: ", Setfile3)
     pickle_in = open(Setfile3, "rb")
     Set = pickle.load(pickle_in)
     for j in range(0, len(Set)):
         print("Passo: ", j + 1, "/", len(Set), " Elementi: ", len(Set[j]))
         IS = []
         for i in range(0, rep + 1):  # numero di ripetizioni
             Set = []
             pickle_in = open(Setfile3, "rb")
             Set = pickle.load(pickle_in)
             SetCopy = Set.copy()
             IS.append(Insertion_sort(Set[j]))
         ISAverage = (statistics.mean(IS))
         print("Il tempo impiegato da Merge Sort (input decr) e': ", ISAverage)
         insertionSortGraph3.append(ISAverage)

     # PLOT

     Set = []
     ElementsNum = []
     pickle_in = open(Setfile1, "rb")
     Set = pickle.load(pickle_in)
     for z in range(0, len(Set)):
         A = Set[z]
         ElementsNum.append(len(A))
     plt.plot(ElementsNum, insertionSortGraph1, '--bo')
     plt.plot(ElementsNum, insertionSortGraph2, '--ro')
     plt.plot(ElementsNum, insertionSortGraph3, '--go')
     plt.xlabel('Numero di elementi')
     plt.ylabel('Tempo di esecuzione')
     plt.title('I casi di insertion sort')
     plt.legend(['Input random', 'Input in ord. crescente', 'Input in ord. decr'])
     plt.grid(True)
     plt.xticks(ElementsNum)
     plt.xticks(rotation=45)
     plt.show()

####################################### SIMULAZIONE #####################################


if __name__ == "__main__":
    # insertion sort best case

    #testComparison(4, "incrBigDataset.pickle")
    #testComparison(900, "incrSmallDataset.pickle")

    # insertion sort worst case

    testComparison(4, "decrBigDataset.pickle")
    testComparison(900, "decrSmallDataset.pickle")

    # average case

    #testComparison(4, "randomBigDataset.pickle")
    #testComparison(2000, "randomSmallDataset.pickle")

    # same algs multiple tests
    #mergeTestComparison(1)
    #insertionTestComparison(4)
