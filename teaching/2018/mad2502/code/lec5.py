"""algorithms discussed on Lecture 5

"""

# Review Quiz 1


# note previous algorithm searches from [0, sqrt(a)], with steps 0.0001. Time sqrt(a) / 0.0001
# a better algorithm binary-searches the same interval [0, sqrt(a)]

# Figure 3.4 Bisection search for square roots (binary search method)
inputstr = input('Enter an integer: ')
a = float(inputstr)
a = abs(a)
allowed_error = 0.01
increase = 0.0001
num_steps = 0
low = 0.0
high = max(1.0, a)
current_guess = (high + low) / 2.0
while abs(current_guess**2 - a) > allowed_error:
    print ('low =', low, 'high =', high, 'guess =', current_guess)
    if (current_guess**2 - a < 0):
        low = current_guess
    else:
        high = current_guess
    current_guess = (high + low) / 2.0    
    num_steps = num_steps + 1
print ('# after ', num_steps, " guesses we get square root of ", a, "is approximated", current_guess)


# how to generalise to more general function? E.g. locating the root for some f(x).


### Chap 4.1. Funcions and scoping


# a simple function that returns x + 1 given x
def add_by_one (x):
    return x + 1


def add_by_two (x):
    tmp = x + 2
    return tmp

    
# function of two/several parameters: a simple function that returns max(x, y)
def max_of_two_values (x, y):
    the_max_element = 0
    if (x > y):
        the_max_element = x
    else:
        the_max_element = y
    return the_max_element


### Chap 4.1.3. Scoping: see scoping.py

# Finally: combining all of above to get bisection.py
