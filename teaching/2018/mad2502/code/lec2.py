# codes on Lecture 2

### Chap 2.2 branching code / conditional statement

# if (Boolean) :
# colon is important
x = 6
if x == 6 :
    print ("yes, x is 6")


# good practice to enclose by parenthesis
x = 6
if (x == 6) :
    print ("yes, x is 6")

    
# several branches
x = 7
if (x % 2 == 0) :
    print ("x is even")
else:
    print ("x is odd")


# error 1: reported by Python
x = 7
if (x % 2 = 0) :
    print ("x is even")
else:
    print ("x is odd")


# error 2: 
x = 7
if (x = 13) :
    print ("x is even")
else:
    print ("x is odd")
    

# several Boolean conditions
x = 3
if (x % 2 == 1) and (x <= 4) :
    print(" x is odd and smaller than 4")
else:
    print("either x>4 or x is even (or both)")

    
# indentation is very important
x = 2
if x == 1 :
    print ("yes, x is 1")
if x % 2 == 0 :
    print ("x is even")
else:
    print ("x is odd")
# compare with this
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


# example: smallest among three
x = 10
y = 4
z = 12
if (x <= y) and (x <= z):
    print ("x is smallest")
elif (y <= z):
    print ("y is smallest")
else:
    print ("z is smallest")

# above does not handle equal case properly!
x = 10
y = 10
z = 12
    

### Chap 2.3 string and input
# double quote == single quote
x = 'a'
type(x)
y = "a"
type(y)


# operator overload
3 * 4
'hello' + 'world'
'hello' + '   world'
100 * 'a'
0 * 'a'
# errors for:
# a
# a * a
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


# (interactive) input
name = str(input("Enter your name: "))
print ("You have typed ", name)
print ("Input has type ", type(name))


# input a number
x = str(input("Enter a number: "))
print ("You have typed ", x)
print ("Input has type ", type(x))
print ("Convert input to int ", int(x))


# pitfall if not converting
x = input("Enter a number: ")
y = 10
print (" 10 * input = ", x * y)


### Chap 2.4 Iteration/loop: while, for
# while(Boolean):
#     do-something

# goal: compute 1 + 2 + 3 + ... + 99


# try the  ``Visualize Python Execution"
# print 1, 2, 3, 4 ... 10
n = 1
while(n <= 10):
    print (" n = ", n)
    n = n + 1

    
# what about?
n = 1
while(n <= 10):
    n = n + 1
    print (" n = ", n)


# close but bug?
total = 0
n = 1
while(n <= 99):
    total = total + n
    print (" adding ", n)


# finally Triangular number
total = 0
n = 1
while(n <= 99):
    total = total + n
    print (" adding ", n)
    n = n + 1
print ("sum is", total)


# combine with user input
total = 0
bound = input("# input upper limit n for summation: ")
bound = int(bound)
n = 1
while(n <= bound):
    total = total + n
    print (" adding ", n)
    n = n + 1
print ("sum is", total)





