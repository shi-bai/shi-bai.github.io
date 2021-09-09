import random
import time

def random_list (n):
    L = []
    for i in range(n):
        L.append(random.randrange(0, 366))
    return L

def sort_select(L):
    n = len(L)
    if (n == 0 or n == 1):
        return L
    for i in range(n):

        # find index of smallest element in [i,..., n]
        min_index = i
        for j in range(i+1, n):
            if (L[min_index] > L[j]):
                min_index = j
                
        # move smallest element to front
        tmp = L[i]
        L[i] = L[min_index]
        L[min_index] = tmp

    return

        
L = random_list (20)
print("# before selection sort", L)
sort_select(L)
print("# after selection sort", L)



def time_sort_select(n):
    L = random_list(n)
    start = time.time()
    sort_select(L)
    end = time.time()    
    print("# select sort |L| = ", n, " took ", end - start)


time_sort_select(100)
time_sort_select(1000)
time_sort_select(10000)




def sort_merge_merging (L1, L2):
    good = []
    i = 0
    j = 0
    while True:
        if (i == len(L1)) and (j == len(L2)):
            break
        elif (i != len(L1) and j != len(L2)):
            if (L1[i] <= L2[j]):
                good.append(L1[i])
                i = i + 1
            else:
                good.append(L2[j])                
                j = j + 1
        elif (j == len(L2)):
            good.append(L1[i])
            i = i + 1
        elif (i == len(L1)):
            good.append(L2[j])
            j = j + 1

    return good


def sort_merge(L):
    n = len(L)
    if (n == 0 or n == 1):
        return L
    else:
        m = len(L)//2
        L1 = sort_merge(L[:m])
        L2 = sort_merge(L[m:])
        return sort_merge_merging(L1,L2)


def time_sort_merge(n):
    L = random_list(n)
    start = time.time()
    L2 = sort_merge(L)
    end = time.time()
    #print(L2)
    print("# merge sort |L| = ", n, " took ", end - start)


time_sort_merge(100)
time_sort_merge(1000)
time_sort_merge(10000)
time_sort_merge(100000)

    
