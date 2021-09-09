"""
detecting primes
"""
import time


# Task 1: primality by trial division
def is_prime_first (n):
    
    if (n <= 0):
        n = -n
    if (n == 2):
        return True
    if (n == 1):
        return False

    for k in range(2, n, 1):
        if (n % k == 0):
            return False

    return True


# note n = 32353 * 42433
n = 1372834849
print ("# n = ", n, ", is_prime(n)=", is_prime_first (n))


# note n = 2 * 682834871
n = 1365669742
print ("# n = ", n, ", is_prime(n)=", is_prime_first (n))



# note n is prime
n = 4253
print ("# n = ", n, ", is_prime(n)=", is_prime_first (n))


# note n is prime
n = 42437
print ("# n = ", n, ", is_prime(n)=", is_prime_first (n))


# note n is prime
n = 424331
print ("# n = ", n, ", is_prime(n)=", is_prime_first (n))


# note n is prime (slow already this example)
n = 42433007
#print ("# n = ", n, ", is_prime(n)=", is_prime_first (n))


"""
n = 13506641086599522334960321627880596993888147560566702752448514385152651060
    48595338339402871505719094417982072821644715513736804197039641917430464965
    89274256239341020864383202110372958725762358509643110564073501508187510676
    59462920556368552947521350085287941637732853390610975054433499981115005697
    7236890927563
"""

# Question: asymptotic running-time of the above algorithm?



def f(x, n):
    return x**2 - n
    
def bisect(f, n, a, b):
    if (f(a, n) * f(b, n) > 0):
        return " input possibly wrong"
    c = (a + b) / 2.0
    tolerance = 0.01
    while ( abs(f(c, n)) > tolerance ):
        if (f(a, n)*f(c, n) < 0):
            b = c
        else:
            a = c
        c = (a + b) / 2.0
    return c


def is_prime_second (n):
    
    if (n <= 0):
        n = -n
    if (n == 2):
        return True
    if (n == 1):
        return False
    
    sqrt_n = bisect(f, n, 0, n)
    sqrt_n = round(sqrt_n) + 1
    
    for k in range(2, sqrt_n, 1):
        if (n % k == 0):
            return False

    return True


# note n is prime
n = 4253
print ("# n = ", n, ", is_prime2(n)=", is_prime_second (n))


# note n is prime
n = 42437
print ("# n = ", n, ", is_prime2(n)=", is_prime_second (n))


# note n is prime
n = 424331
print ("# n = ", n, ", is_prime2(n)=", is_prime_second (n))


# note n is prime (slow already this example)
n = 42433007
print ("# n = ", n, ", is_prime2(n)=", is_prime_second (n))



# Task 2: find all primes upto bound N
def all_primes_below_trial(N):
    L = []
    for n in range(2, N, 1):
        if (is_prime_second(n)):
          L.append(n)  
    return L


# Question: asymptotic running-time of this algorithm?
L = all_primes_below_trial(100)
print(L)


# Sieve of Eratosthenes: first version
def all_prime_below_sieve (N):

    # initialize a list of numbers
    L = []
    for i in range(N):
        L.append(i)

    # 0, 1 are not prime
    L[0] = 0
    L[1] = 0

    # start sieving
    i = 0
    while (i < N):
        if (L[i] != 0):
            p = L[i]
            k = i + p
            while (k < N):
                L[k] = 0
                k = k + p

        i = i + 1

        
    # clean the list
    L2 = []
    for i in range(N):
        if (L[i] != 0):
            L2.append(L[i])
        
    return L2
    
print(all_prime_below_sieve (100))



# Sieve of Eratosthenes: second version
def all_prime_below_sieve2 (N):

    # initialize a list of numbers
    L = []
    for i in range(N):
        L.append(True)

    # 0, 1 are not prime
    L[0] = False
    L[1] = False

    # start sieving
    i = 0
    while (i < N):
        if (L[i]):
            p = i
            k = i + p
            while (k < N):
                L[k] = False
                k = k + p

        i = i + 1

        
    # clean the list
    L2 = []
    for i in range(N):
        if (L[i]):
            L2.append(i)
        
    return L2
    
print(all_prime_below_sieve2 (100))
