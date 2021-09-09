""" Approximate root using the bisection method

"""


def f(x):
    return x**5 - 4*x**3 - x + 7
    #return -(x**5 - 4*x**3 - x + 7)

def bisect_first(a, b):
    ''' Find root of a continuous function f.
    Note one should make sure f(a) * f(b) <= 0
    '''

    if (f(a) * f(b) > 0):
        return " input possibly wrong"

    num_steps = 0
    c = (a + b) / 2.0
    tolerance = 0.01
    while ( abs(f(c)) > tolerance ):
        if (f(c) < 0):
            a = c
        else:
            b = c
        c = (a + b) / 2.0
        num_steps = num_steps + 1

    print ('# after', num_steps, "guesses we approx. the root of the given polynomial is ", c)
    return


# any problem with above code?


def bisect_second(a, b):
    ''' Find root of a continuous function f.
    Note one should make sure f(a) * f(b) <= 0
    '''

    if (f(a) * f(b) > 0):
        return " input possibly wrong"

    num_steps = 0
    c = (a + b) / 2.0
    tolerance = 0.01
    while ( abs(f(c)) > tolerance ):
        # if they have oppo. sign
        if (f(a)*f(c) < 0):
            b = c
        # otherwise f(a)*f(c) > 0   
        else:
            a = c
        c = (a + b) / 2.0
        num_steps = num_steps + 1

    print ('# after', num_steps, "guesses we approx. the root of the given polynomial is ", c)
    return


# first guess a few values to get some interval [a, b]
x = -10
print(" f(", x, ") = ", f(x) )
x = -9
print(" f(", x, ") = ", f(x) )

# better do the guess by a loop
for x in range(-10, 10, 1):
    print(" f(", x, ") = ", f(x) )    

bisect_first(-3, -2)
bisect_second(-3, -2)
