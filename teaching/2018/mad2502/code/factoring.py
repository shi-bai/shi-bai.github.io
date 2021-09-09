"""
Again, recall the trial division we discussed for primality test
"""
def trial_division (n):
    
    if (n <= 0):
        n = -n

    if (n == 1):
        print ("# n = 1")

    # just use the built-in sqrt function
    sqrt_n = round(n**0.5) + 1
    for k in range(2, sqrt_n, 1):
        if (n % k == 0):
            print ("# n =", n, "has a factor k = ", k)
            return
    print ("# n =", n, "is a prime")
    

# the running-time of this algorithm?

# note n is prime
n = 4253
trial_division (n)

print()
print("# some simple numbers")
# note n = 2 * 682834871
n = 1365669742
trial_division (n)

# note n = 3 * 6828348733
n = 20485046199
trial_division (n)

# note n = 3 * 68283487157
n = 204850461471
trial_division (n)

# note n = 7 * 682834871011
n = 4779844097077
trial_division (n)

# note n = 11 * 6828348710011
n = 75111835810121
trial_division (n)

# note n = 13 * 68283487100051
n = 887685332300663
trial_division (n)

# note n =  11 * 682834871000563
n = 7511183581006193
trial_division (n)

print()
print("# some harder numbers")
# note n = 32353 * 42433
n = 1372834849
trial_division (n)

# note n = 879617 * 281063
n = 247227792871
trial_division (n)

# note n = 2375033 * 6251117
n = 14846609161861
trial_division (n)

# note n = 75040657 * 59144821
n = 4438266225987397
trial_division (n)



