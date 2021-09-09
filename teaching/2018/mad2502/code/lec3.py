"""algorithms discussed on Lecture 3

"""


# summation with user input as bound
# Question: how many operations does the algorithm do?
total = 0
bound = input("# input upper limit n for summation: ")
bound = int(bound)
n = 1
while(n <= bound):
    total = total + n
    #print (" .. adding ", n)
    n = n + 1
print ("# sum is", total)


# Try a simpler version
total = 0
bound = input("# input upper limit n: ")
bound = int(bound)
n = 1
while(n <= bound):
    n = n + 1
print ("# completed ", bound, " many operations")


# how many (simple) operations can a computer do in seconds?
# timing module: see https://docs.python.org/3/library/index.html
import time
start = time.time()
print(" do something ")
end = time.time()
print (" time elapsed ", end - start)


# Example 1: simple benchmarking: add timing to above loop
import time
total = 0
bound = input("# input upper limit n: ")
x = int(bound)
n = 1
start = time.time()
while(n <= x):
    n = n + 1
end = time.time()    
print ("# completed ", x, " many operations in", end-start, " seconds")


### Chap 3.1. print one/the cubic root of x when x = k^3
# Question: how many operations does this algorithm do?
inputstr = input('Enter an integer: ')
x = int(inputstr)
x = abs(x)
k = 0
# try all k such that k^3 < x
while (k**3 < abs(x)):
    k = k + 1

# then k^3 > x or k^3 = x
if (k**3 == abs(x)):
    if (x < 0):
        k = -k
    print ('cubic root of ', x, 'is', k)
else:
    print ('x is not a perfect cube')    


    
### Chap 3.2. for loop
# for Variable in range(start, end, step):
bound = 4
for i in range(0, bound, 1):
    print(i)

bound = 4
for i in range(0, bound, 2):
    print(i)


# note the last element is the largest such integer start + i * step
# that is strictly smaller than end
bound = 4
for i in range(0, bound, 4):
    print(i)


##########################
# now intro to big-O notation


