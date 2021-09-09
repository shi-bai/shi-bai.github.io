"""
some examples of recursion

rule of thumb: remember to write the terminating condition!
"""

# we've done this in assignment 1. but here we use recursion.
def factorial (n):
    """
    Compute the factorial of n.
    """

    if (n <= 1):
        return 1
    else:
        return factorial(n-1) * n


a = 5
result = factorial (a)
print ("factorial of", a, " is ", result)
a = 0
result = factorial (a)
print ("factorial of", a, " is ", result)
a = 2
result = factorial (a)
print ("factorial of", a, " is ", result)




# we've done this in the first quiz, here we use recursion
def Fibonacci(n):
    """
    Compute the n-th Fibonacci number.
    Start with x_1 = 1 and x_2 = 1 and
    then definition x_i = x_{i-1} + x_{i-2} for i >= 3
    """
    if (n < 0):
        return 0
    if( n <= 2):
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)


print("# the 4-th Fib. number is ", Fibonacci(4))


def first_m_Fibonacci(m):
    """
    Above only generate the n-th Fib. number.
    Here we print 1 to the m-th Fib. number.
    """
    for i in range(1, m+1):
        print(Fibonacci(i))


first_m_Fibonacci(10)        


# the recurrence relation could also be defined on pairs
# Binomial coefficient n choose k
def binom(n, k):
    """
    binomial coefficient 
    C(n, k) = n! / (k! * (n-k)!)
    Use the recursive identity (Pascal's triangle)
    C(n,k) = C(n-1,k-1) + C(n-1,k)
    """
    if (k > n or n < 0 or k < 0):
        return "not defined"
    # now n >= k >= 0
    if (k == 0):
        return 1
    if (n == 0):
        return 1
    # now n, k > 0
    if (n == k):
        return 1
    return binom(n-1,k-1) + binom(n-1,k)


n = 6
k = 3
result = binom (n, k)
print ("C (", n, ", ", k, ") = ", result)
print ()

def test_binom(n):
    for k in range(n+1):
        print (binom(n, k)), " "


test_binom(7)        
