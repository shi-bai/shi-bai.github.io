"""operators

This file shows basic usage of operators in Python.

    arithmetic operators;
    comparison operators;
    logical    operators;
    assignment operators;

"""

x = 3
y = 7
print ("x = 3")
print ("y = 7")
print("")

# arithmetic operators returns int, float type
print("x + y =", x+y)
print("x - y =", x-y)
print("x * y =", x*y)
print("x / y =", x/y)
print("x // y =", x//y)
print("x ** y =", x**y)
print("")


# comparison operator returns Boolean type
x = 3
y = 7
print("x > y   returns",  x > y)
print("x >= y  returns",  x >= y)
print("x < y   returns", x < y)
print("x <= y  returns", x <= y)
print("x == y  returns", x == y)
print("x != y  returns", x != y)
print("")

# logical operator: usually on two Boolean returns Boolean
x = True
y = False
print("x and y returns", (x and y))
print("x and y returns", (x or y))
print("NOT x returns", not x)
print("NOT y returns", not y)


# assignment
x = 1
x = x + 1
x = x - 1
x = x * 2
x = x / 2
