"""
simple Euclidean algorithm
"""

# also check if a > b
def Euclidean (a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a


def ext_Euclidean (a, b):
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1
    while (b != 0):
        q = a // b # also quotient
        r = a % b
        a = b
        b = r

        tmp = x0 - q * x1
        x0 = x1
        x1 = tmp

        tmp = y0 - q * y1
        y0 = y1
        y1 = tmp
        
    return  a, x0, y0
