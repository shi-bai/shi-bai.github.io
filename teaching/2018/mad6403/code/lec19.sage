"""
birthday paradox idea 

"""

import random


# this function was copied from a previous lecture
def random_birthday (n):
    return random.randrange(0, n)


# generate_random_x_y (247227792871)
def generate_random_x_y (N):
    all_birthdays = []
    trials = 0
    while (True):
        x = random_birthday(N)
        trials = trials + 1

        # compare x with all y in current list
        for i in range(len(all_birthdays)):
            y = all_birthdays[i]
            g = gcd(x-y, N)
            if (g > 1 and g < N):
                print("# success! found (x, y) =", x, y, " after ", trials, " trials")
                return x, y, g, N/g
            
        # if not match between x and current list, append it    
        all_birthdays.append(x)
        
    return



"""
Pollard's rho method for factoring

"""

def f(x, N):
    return (x**2 + 1) % N

# Pollard_rho (247227792871, random_birthday(N))
def Pollard_rho (N, x):
    y = x
    trials = 0
    while (True):
        x = f(x, N)
        y = f(f(y, N), N)
        trials = trials + 1
        g = gcd((x - y) % N, N)
        if (g > 1 and g < N):
            print("# success! found (x, y) =", x, y, " after ", trials, " trials")
            return x, y
