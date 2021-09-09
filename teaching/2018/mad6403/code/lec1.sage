### Lec 1: very basics of Sagemath

# The hash character marks the beginning of a comment. Any text after will be ignored until the end of the line

''' This is another way of commenting,
      in particular for
      multiple line '''

""" this is also
  ok """


# This is the first code: print something
print("This line will be printed.")
print "This line is also ok."

# Try several letters
print 'three letters', "are also", 'ok'


# sage as a calculator
1 + 1
(1 + 4 * (3 + 10)) * 2
1 / 3
1 / 3.0
i = 10
j = 5
k = 2
print "# i = ", i
print "# j = ", j
print "# k = ", k
print i, "x", j, "=", i*j
print k, "-", j, "=", k-j
print j, "//", k, "=", j//k
print k, "+", j, "=", k+j
print i, "%", j, "=", i%j
print j, "%", k, "=", j%k


# exponentiation
print (i**j)
print (i **  j)
print (i^j)


# elementary funcs
sin(pi/3)
exp(2)
exp(2.0)
n(exp(2))
sin(10).n(digits=5)
numerical_approx(pi, prec=200)


# basic types
type(i)
type(1)
type(1.0)
type(2**3)
type(1/3)
type(0.33333)
x = 10
y = 3
print(type(x/y))
print(type(x//y))
ss = 'hello'
type(ss)

# boolean type
a = False
b = True
a = 1
a == 1
type(a == 1)
bool(10)
bool(10.0)
bool(0.1)
bool(0.00001)
bool(1e-1000)

# usual precedence order
print (100 + 1 * 2)
print ( (100 + 1) * 2 )


# There is no limit to the size of integers or rational numbers (upto memory)
x = 7.5
y = 2.5
print "sqrt(x) =", sqrt(x)
print "x^(1/3) =", x^(1/3)
print "x^(1/1000) =", x^(1/1000)


# precision of floating point types， careful with == for floating point types
1.13 - 1.1
a = 1e11
print((a-1) * (a+1) == a*a)
0 == 0.00000000000000000000000000000001
0.0 == 1e-100
0.0 == 1e-1000


# Python type
a = 10.9
int(a)
a = 10
float(a)


##################### simple branching code / conditional statement ##################### 
x = 2
if x == 1 :
    print ("yes, x is 1")

x = 3
if x % 2 == 0 :
    print ("x is even")
else:
    print ("x is odd")
    


# (Python) indentation is important
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
    

# double quote == single quote
'a'
"a"
3 * 4

# operator overload
'a' + 'b'
100 * 'a'

# errors with
# 'a' * 'a'


# reference
x = "hello world"
len(x)


# index reference starts from 0
print("first character in string x is", x[0])
print("last character in string x is", x[10])
print("last character in string x is", x[len(x)-1])


# slicing
print (x[0:0])
print (x[0:1])
print (x[0:10])
print (x[0:11])
print (x[0:len(x)])



# while-loop
# while(Boolean):
#     do-something


# goal: output 1, 2, 3, ..., 99 consecutively
n = 1
while(n <= 10):
    print " n = ", n
    n = n + 1

    
# goal: compute the sum 1 + 2 + 3 + ... + 99 
total = 0
n = 1
while(n <= 10):
    total = total + n
    print " -- adding ", n
    n = n + 1
print "sum is", total
    

# help
sin?
help(sin)


# plot(sin(2*z), z, -pi, pi)


# an integer is stored as a chunk of bits in computer
a = 100
print a.bits()

# computer do arithmetic a fixed chunk of bits (e.g. 64 bits)
