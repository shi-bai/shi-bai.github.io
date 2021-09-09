# The hash character marks the beginning of a comment. Any text after will be ignored until the end of the line

# IDLE has two modes: as an interactive shell and a text-editor

''' This is another way of commenting,
      in particular for
      multiple line '''

""" this is also
  ok """


# This is the first code: print something
print("This line will be printed.")


# This is incorrect syntax in Python 3, but ok in Python 2
# print "this is incorrect in Python 3"


# Try single quote
print ('Single quote is also fine')


# Try several letters
print ('three letters', "are also", 'ok')


# whitespace-sensitive: not allowed --> unexpected indent
#   print("no white space")


##################### Chap 2.1 ##################### 
# Python has 4 basic build-in objects for arithmetic
# int, float bool, None

# 1. integer type
print("# Examples of arithmetic using integer data type")

i = 10
j = 5
k = 2
print ("# i = ", i)
print ("# j = ", j)
print ("# k = ", k)

print(i, "x", j, "=", i*j)
print(k, "-", j, "=", k-j)
print(j, "//", k, "=", j//k)
print(k, "+", j, "=", k+j)
print(i, "%", j, "=", i%j)
print(j, "%", k, "=", j%k)


# exponentiation
print(i**j)
print (i **  j)

# boolean type
a = False
b = True
a = 1
a == 1
type(a == 1)


# 2. floating point types
print("# Examples of arithmetic using floating point type")
x = 10.0
y = 5.0
z = 2.0
print("x = ", x)
print("y = ", y)
print("z = ", z)

print(x, "/", y, "=", x/y)
print(y, "/", x, "=", y/x)
print(y, "/", z, "=", y/z)
print(z, "/", y, "=", z/y)

print("examples of mathematical functions")
x = 7.5
y = 2.5

print("x = ", x)
print("y = ", y)
print(x, "^", y, "=", x**y)


# auto cast
x = 10
y = 3
print(type(x/y))
print(type(x//y))


# usual precedence order
print (100 + 1 * 2)
print ( (100 + 1) * 2 )


# extra math functions you need extra packages
import math
x = 7.5
y = 2.5
print("x = ", x)
print("y = ", y)
print(x, "^", y, "=", x**y)
print("exp(", x, ") =", math.exp(x))
print("ln(", x, ") =", math.log(x))
print("tan(", y, ") =", math.tan(y))
print("sqrt(", y, ") =", math.sqrt(y))
print(" constant pi is", math.pi)
print(" constant e is", math.e)


# precision of floating point types， careful with == for floating point types
1.13 - 1.1
a = 1e11
print((a-1) * (a+1) == a*a)
0 == 0.00000000000000000000000000000001
0.0 == 1e-100
0.0 == 1e-1000


# type conversion
a = 10.9
int(a)
a = 10
float(a)
bool(10)
bool(10.0)
bool(0.1)
bool(0.00001)
bool(1e-1000)

##################### Chap 2.2 branching code / conditional statement ##################### 
x = 2
if x == 1 :
    print ("yes, x is 1")

x = 3
if x % 2 == 0 :
    print ("x is even")
else:
    print ("x is odd")
    


# indentation is important
x = 2
if x == 1 :
    print ("yes, x is 1")
    if x % 2 == 0 :
        print ("x is even")
    else:
        print ("x is odd")


# more branches
x = 3
if (x == 1):
    print("x is 1")
elif (x == 2):
    print("x is 2")
elif (x == 3):
    print ("x is 3")
else:
    print ("I am enough")


# more conditions
x = 10
y = 4
z = 12
if (x < y) and (x < z):
    print ("x is smallest")
elif (y < z):
    print ("y is smallest")
else:
    print ("z is smallests")
    

##################### Chap 2.3 string and input ##################### 
# double quote == single quote
'a'
"a"
3 * 4

# operator overload
'a' + 'b'

100 * 'a'

# errors with
# a
# a * a
# 'a' * 'a'

