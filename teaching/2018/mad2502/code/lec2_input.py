"""
A script to illustrate the usage of the input command in python
"""

# first example
person = input('enter your name: ')
print('Hello', person)
print('input has type')


# some computations
input_string = input("enter the value of x: ")
x = int(input_string)
print("the value of x is ",x)

input_string = input("enter the value of y: ")
y = int(input_string)
print("the value of y is ",y)

## perform some calculations
print("computations")    
print(x, "+", y, "=",x+y)
print(x, "*", y, "=",x*y)
print(y, "-", x, "=",y-x)
print(x, "-", y, "=",x-y)
print(y, "//", x, "=",y//x)
print(x, "//", y, "=",x//y)
print(y, "/", x, "=",y/x)
print(x, "/", y, "=",x/y)
