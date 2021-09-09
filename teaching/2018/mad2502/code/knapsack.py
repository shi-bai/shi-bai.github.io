import random
import time
import itertools


def random_numbers (n, M):
    L = []
    for i in range(n):
        L.append(random.randrange(0, M))
    return L


def random_01 (n):
    L = []
    for i in range(n):
        L.append(random.randrange(0, 2))
    return L



def create_knapsack (n, M):
    a = random_numbers(n, M)
    x = random_01(n)

    # find a0 * x0 + a1 * x1 + a2 * x2 ...
    t = 0
    for i in range(n):
        t = t + a[i] * x[i]
    return a, x, t




# problem: given a and t, find x?
# note there are at most 2^n such x

# first idea: exhaustive search/try them all!

def check_x (a, t, x):
    n = len(a)
    t2 = 0
    for i in range(n):
        t2 = t2 + a[i] * x[i]
    if (t2 == t):
        return True
    else:
        return False
    
    

def solve_knapsack_exhaustive (a, t, sol):
    n = len(a)

    # use itertools library to generate all combinations
    all_possible = list(itertools.product([0, 1], repeat=n))
    
    # try all of them, 1 by 1
    for i in range(2**n):
        x = all_possible[i]
        if (check_x (a, t, x)):
            print("# found solution x = ", x)
            return x
                
    print ("# solution does not exist")
    return
    

def create_and_solve_exhaustive (n):
    a, x, t = create_knapsack (n, 2**n)
    print("# solving n = ", n, " using exhaustive search")    
    print("# a = ", a)
    print("# x = ", x)
    print("# t = ", t)
    solve_knapsack_exhaustive (a, t, x)



# second idea: meet in the middle attack
def sum_ax (a, x):
    n = len(a)
    t = 0
    for i in range(n):
        t = t + a[i] * x[i]
    return t


def solve_knapsack_MIM (a, t, sol):
    # assume n is even
    n = len(a)
    
    Ln = n // 2
    La = a[:Ln]

    Rn = n - Ln
    Ra = a[Ln:]
    
    # use itertools library to generate all combinations
    all_possible_L = list(itertools.product([0, 1], repeat=Ln))
    all_possible_R = list(itertools.product([0, 1], repeat=Rn))
    

    # build L_t
    L_t = []
    # try all of them, 1 by 1
    for i in range(2**Ln):
        tmp = []
        lt = sum_ax(La, all_possible_L[i])
        tmp.append(lt)
        tmp.append(i)        
        L_t.append(tmp)

    # build R_t similarly
    R_t = []
    # try all of them, 1 by 1
    for i in range(2**Rn):
        tmp = []
        rt = sum_ax(Ra, all_possible_R[i])
        tmp.append(t-rt)
        tmp.append(i)        
        R_t.append(tmp)        
    print (all_possible_L)
    print(L_t)
    print(R_t)
    # now we have two list of numbers L_t and R_t
    L_t.sort()
    R_t.sort()
    #print (L_t)
    #print (R_t)

    # finally search for the match
    i = 0
    j = 0
    while (True):
        if (L_t[i][0] == R_t[j][0]):
            il = L_t[i][1]
            ir = R_t[j][1]            
            lx = all_possible_L[il]
            rx = all_possible_R[ir]
            break
        elif (L_t[i] < R_t[j]):
            i = i + 1
            
        else:
            j = j + 1            
    
    x = lx + rx
    print("# found solution x = ", x)    
                
    return
    

def create_and_solve_MIM (n):
    a, x, t = create_knapsack (n, 2**n)
    print("# solving n = ", n, " using meet-in-the-middle")        
    print("# a = ", a)
    print("# x = ", x)
    print("# t = ", t)
    solve_knapsack_MIM (a, t, x)


print()
create_and_solve_MIM (4)
#print()
#create_and_solve_MIM (20)
