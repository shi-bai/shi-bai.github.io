### Chap 4.1. Funcions and scoping
some_variable = 99
i = 0
while (i < 10):
    i = i + 1
    print(some_variable)


""" what are the outputs?
i = 0
while (i < 10):
    some_variable = 99
    i = i + 1
    print(some_variable)


i = 0
while (i < 10):
    some_variable = 99
    i = i + 1
print(some_variable)


i = 0
while (i < 10):
    some_variable = 99
i = i + 1
print(some_variable)

"""

# variables in function
def f(x):
    # y is local variable
    y = 1
    x = x + y
    print ('inside function x = ', x)
    return x

x = 3
y = 2
z = f(x)
print ('z =', z)
print ('x =', x)
print ('y =', y)

