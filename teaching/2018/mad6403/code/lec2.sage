### Lec 2

# a simple function that returns x + 1 given x
def add_by_one (x):
    return x + 1

add_by_one(10)

def add_by_two (x):
    tmp = x + 2
    return tmp

add_by_one(10)


# function of two/several parameters: a simple function that returns max(x, y)
def max_of_two_values (x, y):
    the_max_element = 0
    if (x > y):
        the_max_element = x
    else:
        the_max_element = y
    return the_max_element

max_of_two_values(10, -3)


# convert an integer in base 10 to base 2^64
def integer_to_base2_64 (n):
    newn = []
    if n < 0:
        sign = -1
        n = -n
    elif n == 0:
        return 1, [0]
    else:
        sign = 1
    while (n > 0):
        a_i = n % (2**64)
        newn.append (a_i)
        n = n // (2**64)
    return sign, newn

integer_to_base2_64 (0)
integer_to_base2_64 (1)
integer_to_base2_64 (1000)
integer_to_base2_64 (2**64-1)
integer_to_base2_64 (2**64)
integer_to_base2_64 (2**64+1)


def integer_from_base2_64 (sign, list_n):
    n = 0
    i = 0
    print list_n
    for x in list_n:
        n = n + x * (2^64)^i
        i = i + 1
    
    return n * sign


r = ZZ.random_element(0,2^1024)
print r

sign,r_base64 = integer_to_base2_64 (r)
print r_base64

r2 = integer_from_base2_64 (sign, r_base64)
print r2



# simulate adding of two mp numbers
def add_two_mp (a, b):
    
    sign_a, list_a = integer_to_base2_64 (a)
    sign_b, list_b = integer_to_base2_64 (b)
    assert(sign_a == sign_b)
    
    while (len(list_a) < len(list_b)):
        list_a.append(0)
    while (len(list_b) < len(list_a)):
        list_b.append(0)

    carry = 0
    list_c = []
    for i in range(len(list_a)):
        tmp = list_a[i] + list_b[i] + carry
        carry = 0
        if (tmp >= 2**64):
            tmp = tmp - 2**64
            carry = 1
        list_c.append(tmp)

    if carry == 1:
        list_c.append(1)

    c = integer_from_base2_64 (sign, list_c)    
        
    return c
    
            

# set random seed
#set_random_seed(0)
ll = 1024
a = ZZ.random_element(0,2^ll)
b = ZZ.random_element(0,2^ll)
c = add_two_mp (a, b)
print a + b     
print c
