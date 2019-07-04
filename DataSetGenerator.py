import random
import math
import pickle

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


def multiple_random_vect(MultipleNumberVect, step1, multi):
    numbervect1 = []
    for i in range(multi+1):
        numbervect1.append(i*step1)
    for j in range(len(numbervect1)):
        MultipleNumberVect.append(random_vect(numbervect1[j]))
    return MultipleNumberVect

def multiple_incr_vect(MultipleNumberVect, step1, multi):
    numbervect1 = []
    for i in range(multi+1):
        numbervect1.append(i*step1)
    for j in range(len(numbervect1)):
        MultipleNumberVect.append(incr_vect(numbervect1[j]))
    return MultipleNumberVect

def multiple_decr_vect(MultipleNumberVect, step1, multi):
    numbervect1 = []
    for i in range(multi+1):
        numbervect1.append(i*step1)
    for j in range(len(numbervect1)):
        MultipleNumberVect.append(decr_vect(numbervect1[j]))
    return MultipleNumberVect



# ATTENZIONE, NON ESEGUIRE QUESTO FILE: IL DATASET DI BASE VIENE MODIFICATO !!!
# Standard Data set to compare algs

##################### RANDOM BIG DATA SET #######################
SavedDataSet = []
multiple_random_vect(SavedDataSet, 5000, 20)
pickle_out = open("randomBigDataset.pickle", "wb")
pickle.dump(SavedDataSet, pickle_out)
pickle_out.close()

################### INCREASING ORD BIG DATA SET #######################
SavedDataSet = []
multiple_incr_vect(SavedDataSet, 5000, 20)
pickle_out = open("incrBigDataset.pickle", "wb")
pickle.dump(SavedDataSet, pickle_out)
pickle_out.close()

################### DECREASING ORD BIG DATA SET ######################
SavedDataSet = []
multiple_decr_vect(SavedDataSet, 5000, 20)
pickle_out = open("decrBigDataset.pickle", "wb")
pickle.dump(SavedDataSet, pickle_out)
pickle_out.close()

##################### RANDOM SMALL DATA SET #######################
SavedDataSet = []
multiple_random_vect(SavedDataSet, 40, 5)
pickle_out = open("randomSmallDataset.pickle", "wb")
pickle.dump(SavedDataSet, pickle_out)
pickle_out.close()

################### INCREASING ORD SMALL DATA SET #######################
SavedDataSet = []
multiple_incr_vect(SavedDataSet, 40, 5)
pickle_out = open("incrSmallDataset.pickle", "wb")
pickle.dump(SavedDataSet, pickle_out)
pickle_out.close()

################### DECREASING ORD SMALL DATA SET ######################
SavedDataSet = []
multiple_decr_vect(SavedDataSet, 40, 5)
pickle_out = open("decrSmallDataset.pickle", "wb")
pickle.dump(SavedDataSet, pickle_out)
pickle_out.close()


print("DATASET IS NOW REFRESHED")



