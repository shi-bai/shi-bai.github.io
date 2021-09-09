"""
Euclidean algorithm
"""



def Euclidean (a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a

print(Euclidean(100, 44))

def EuclideanRec (a, b):
    if (b == 0):
        return a
    else:
        return EuclideanRec(b, a % b)

print(EuclideanRec(100, 44))    


