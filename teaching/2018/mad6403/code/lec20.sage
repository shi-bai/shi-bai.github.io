# Fermat_method (1649)
def Fermat_method (N):
    x = ceil(sqrt(N))

    while (1):
        y2 = x^2 % N
        #print "x =", x, " x^2 (mod N) = ", factor(y2)
        if (is_square(y2) == True):
            y = sqrt(y2)
            break
        x = x + 1
        
    print "# x = ", x
    print "# y = ", y
    print "# gcd(x+y, N)", gcd(x+y, N)
    print "# gcd(x-y, N)", gcd(x-y, N)    


# aux_factor_base (20)
def aux_factor_base (B):
    S = []
    p = 2
    while (p < B):
        S.append(p)
        p = next_prime(p)
    return S


# return empty list [] if it can not be completed factored by p in S
def trial_division (y, S):
    factors = []
    for p in S:
        while (y % p == 0):
            factors.append(p)
            y = y // p
            if (y == 1):
                return factors
    return []


# Dixon_method (1649)
def Dixon_method (N):
    S = aux_factor_base (20)
    x = ceil(sqrt(N))
    relations_y = []    
    relations_factor = []

    c = 0
    while (c < len(S)):
        y2 = x^2 % N
        factors = trial_division (y2, S)
        if (len(factors) > 0):
            relations_y.append(y2)
            relations_factor.append(factors)
            c = c + 1
        x = x + 1
    return relations_y, relations_factor

    
