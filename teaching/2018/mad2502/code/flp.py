import math

"""
examples of binary/decimal numbers; floating-point numbers
"""


def bin2dec(l):
    """
    convert n (binary) in str to its decimal representation
    -- works only for integral input l
    """
    n = len(l)
    d = 0
    for i in range(n):
        d = d + int(l[i]) * 2**(n-i-1)
    print ("# decimal of l =", l, "is", d)
    return d

bin2dec("101001")
bin2dec("111")


def dec2bin_print(n):
    """
    convert n (decimal) to its binary representation (just print)
    -- works only for integral input n
    """

    if (n > 1):
        dec2bin_print(n//2)
    print (n % 2)
    
    return

dec2bin_print(41)
print()
dec2bin_print(7)


def dec2bin(n):
    """
    convert n (decimal) to its binary representation in a string
    -- works only for integral input n
    """

    if (n == 1):
        return '1'
    else:
        return dec2bin(n//2) + str(n%2)

print(dec2bin(41))
print(dec2bin(7))



def dec2bin_fractional (f):
    """
    econvert n (decimal) to its binary representation
    -- works only for fractional input f < 1.0
    """    

    if (f >= 1.0):
        return
    
    bin_f = '0.'
    while f > 0:

        if (f == 0):
            break
        
        # upto precision 53 bits (mantissa)
        if len(bin_f) >= 53:
            break

        curr_bit = math.floor(f * 2.0)
        bin_f = bin_f + str(curr_bit)
        f = f * 2.0 - math.floor(f * 2.0)
        
    return bin_f


print(dec2bin_fractional (0.625))
print(dec2bin_fractional (0.1))


"""
Reference: https://docs.python.org/2/tutorial/floatingpoint.html

Python only prints a decimal approximation to the true decimal value of the binary approximation stored by the machine. If Python were to print the true decimal value of the binary approximation stored for 0.1, it would have to display
>>> 0.1
0.1000000000000000055511151231257827021181583404541015625
That is more digits than most people find useful, so Python keeps the number of digits manageable by displaying a rounded value instead
>>> 0.1
0.1

"""

# gives 0.30000000000000004
print("# 0.1 + 0.2 = ", 0.1 + 0.2)


