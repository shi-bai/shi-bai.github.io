"""
Factoring with the birthday paradox idea 

Idea: try to generate random elements (mod n) and take gcd(pairs, n)
"""

import random

# this function was copied from a previous lecture
def Euclidean (a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a


# this function was copied from a previous lecture
def random_birthday (n):
    return random.randrange(0, n)

def run_game_once (n):
    all_birthdays = []
    trials = 0
    while (True):
        x = random_birthday(n)
        trials = trials + 1

        # compare x with all y in current list
        for i in range(len(all_birthdays)):
            y = all_birthdays[i]
            gcd = Euclidean(x-y, n)
            if (gcd > 1 and gcd < n):
                print("# success! found (x, y) =", x, y, " after ", trials, " trials")
                return x, y
            
        # if not match between x and current list, append it    
        all_birthdays.append(x)
        
    return


n = 247227792871
x, y = run_game_once (n)
print("# factor of", n, "is ", Euclidean(x-y, n))
print()

n = 4438266225987397
# this is slow
#x, y = run_game_once (n)



"""
Pollard's rho method for factoring

Idea: generate a sequence in a good pattern such that one can find
      the collision in a much faster fashion.
"""

def f(x, n):
    return (x**2 + 1) % n

def Pollard_rho (n, x):
    y = x
    trials = 0
    while (True):
        x = f(x, n)
        y = f(f(y, n), n)
        trials = trials + 1
        gcd = Euclidean((x - y)%n, n)
        if (gcd > 1 and gcd < n):
            print("# success! found (x, y) =", x, y, " after ", trials, " trials")            
            return x, y


n = 247227792871
x, y = Pollard_rho (n, 1)
print("# factor of", n, "is ", Euclidean(x-y, n))
print()

# now this is faster
n = 4438266225987397
x, y = Pollard_rho (n, 1)
print("# factor of", n, "is ", Euclidean(x-y, n))
print()

# try larger
n = 448364695764698077
x, y = Pollard_rho (n, 1)
print("# factor of", n, "is ", Euclidean(x-y, n))
print()


n = 14677883308230845957
x, y = Pollard_rho (n, 1)
print("# factor of", n, "is ", Euclidean(x-y, n))
print()


n = 74303811947833831102510333
x, y = Pollard_rho (n, 1)
print("# factor of", n, "is ", Euclidean(x-y, n))
print()
