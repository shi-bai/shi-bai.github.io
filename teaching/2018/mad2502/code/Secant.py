# root-finding by Newton and secant methods
# import math
from math import sin, cos
import time
tolerance = 0.0001

# example: a non-polynomial function. 
def non_poly_func(x):
    return x**2 + cos(x)**7 + 2*sin(x)
def non_poly_func_der(x):
    return 2*x - 7 * cos(x)**6 * sin(x) + 2 * cos(x)


# example: a poly that Newton converges slow
def slow_poly_func(x):
    return x**20 - 1
def slow_poly_func_der(x):
    return 20*x**19


# Newton's method (copied from the last lecture)
# Note: Newton's method evalutes both f(x) and f'(x)
def Newton_method (f, f_derivative, x):
    initial = x
    num_steps = 0
    while (abs(f(x)) > tolerance):
        # update with a new guess x
        x = x - f(x) / f_derivative(x)
        num_steps = num_steps + 1
    #print ('# [Newton] initial = ', initial, ' after', num_steps, "steps, approx. root is ", x)
    return x


r1 = Newton_method (non_poly_func, non_poly_func_der, 1)
print("# |f(r)| is ", non_poly_func(r1))
print()

r2 = Newton_method (slow_poly_func, slow_poly_func_der, 0.2)
print("# |f(r)| is ", slow_poly_func(r2))
print()


# A variant of Newton's method that does not need derivative;
#  use finite difference/numerical differentiation instead.
def Newton_finite_difference (f, f_derivative, x):
    initial = x
    num_steps = 0
    h = 0.01
    while (abs(f(x)) > tolerance):
        # the f_derivative is only used for comparison purpose
        true_dx = f_derivative(x)
        approx_dx = (f(x+h) - f(x)) / h
        x = x - f(x) / approx_dx
        num_steps = num_steps + 1
    #print ('# [Newton_finite_difference] initial = ', initial, ' after', \
    #           num_steps, "steps, approx. root is ", x)
    return x


r3 = Newton_finite_difference (non_poly_func, non_poly_func_der, 1)
print("# |f(r)| is ", non_poly_func(r3))
print()



# the secant method
def secant(f, x0, x1):
    initial_x0 = x0
    initial_x1 = x1
    y0 = f(x0)
    y1 = f(x1)
    num_steps = 0
    while (abs(y1) > tolerance):
        # y1 /  (x1 - x0) / (y1 - y0)
        x2 = x1 - y1 * (x1-x0) / (y1-y0)

        # updates
        x0 = x1
        x1 = x2
        #y0 = f(x0) # <-- important that this NOT needed (to save running-time)
        y0 = y1
        y1 = f(x1)        

        num_steps = num_steps + 1
        
    # done
    #print ('# [Secant] x0 = ', initial_x0, 'x1 = ', initial_x1, ' after', \
    #           num_steps, "steps, approx. root is ", x1)
    return x1


r4 = secant (non_poly_func, 1, 1.01)
print("# |f(r)| is ", non_poly_func(r4))
print()



# secant could be faster as it involves less evaluations
def compare_time():

    #  run above Newton's method for many times
    start = time.time()
    for i in range(50000):
        Newton_method (non_poly_func, non_poly_func_der, 1)
    Newton_end = time.time() - start
    
    # run above secant method for many times
    start = time.time()
    for i in range(50000):
        secant (non_poly_func, 1, 1.01)
    secant_end = time.time() - start

    print ("# Newton time = ", Newton_end)
    print ("# secant time = ", secant_end)

compare_time()    
