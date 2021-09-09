"""
R.<x> = PolynomialRing(GF(7))
f(x) = x*(x+5)*(x+6)*(x^2 + 6*x + 4)*(x^2 + 4*x + 5)*(x^3 + x^2 + 4*x + 6)*(x^3 + 4*x^2 + 5*x + 5)
f = R(f(x).expand())
f.factor()


G1 = gcd(x^7-x, f)
f2 = f / G1

G2 = gcd(x^49-x, f2)
f3 = f2 / G2

G3 = gcd(x^343-x, f3)
f4 = f3 / G3
"""
# f4 is 1 now.



# f = generate_some_f(next_prime(1007), 10)
def generate_some_f(p, r):
    R.<x> = PolynomialRing(GF(p))
    f = 1
    for i in range(r):
        randeg = randint(1, 5) # irreducible factor at most degree 5
        g = R.irreducible_element(randeg, "random")
        f = f * g
    return f


# factors =  distinct_degree(f)
def distinct_degree(f):
    p = f.base_ring().cardinality()
    R.<x> = PolynomialRing(GF(p))    
    factors = []
    a = x
    while (1):
        a = a^p % f # shoud use repeated squaring
        tmp = gcd(a - x, f)
        factors.append(tmp)
        f = f // tmp
        if (f == 1):
            return factors


def power_a_mod_f(a, e, f):
    x = a
    l = e
    temp = 1
    while (l > 0):
        while ( (l % 2) == 0):
            x = (x * x) % f
            l = l // 2
        temp = (temp * x) % f
        l -= 1
    return temp 
        
        
# Cantor-Zassenhaus
def equal_degree_one(f, d):
    R  = f.base_ring()
    p = R.cardinality()
    print d
    a = parent(f).random_element((1, f.degree()))
    # random monic
    a = a.monic()
    e = (p^d - 1)//2
    tmp = power_a_mod_f(a, e, f)
    output = gcd(tmp-1, f)
    
    if (output.degree() == d):
        return output
    else:
        return -1
    

# loop over all factors after distinct degree factorization
# equal_degree(factors)
def equal_degree(factors):
    
    for i in range(len(factors)):
        g = factors[i]
        if (g.degree() <= i+1):
            continue
        else:
            equal_degree_one(g, i+1)


        
# test_factoring(next_prime(1007), 10)
def test_factoring(p, r):
    f = generate_some_f(next_prime(p), r)
    factors = distinct_degree(f)
    return factors
    
        
