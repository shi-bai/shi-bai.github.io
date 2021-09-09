# plot timing comparison

import time

# compare_timings (2000)
def compare_timings (max_n):

    num_trials_each = 10
    
    R = QQ[x]
    time_classic = []
    time_Karatsuba = []
    
    for n in range(500, max_n, 100):
        print n
        time_c = 0
        time_K = 0
        
        for i in range(num_trials_each):

            f = R.random_element(n)
            g = R.random_element(n)

            # timing classic
            start = time.time()
            f._mul_generic(g)
            end = time.time()
            time_c = time_c + (end - start) 

            # timing Karatsuba            
            start = time.time()
            f._mul_karatsuba(g)
            end = time.time()
            time_K = time_K + (end - start) 

        time_c = RR(time_c / num_trials_each)
        time_K = RR(time_K / num_trials_each)
        
        time_classic.append(time_c)
        time_Karatsuba.append(time_K)


    return time_classic, time_Karatsuba
# result of 
# compare_timings (2000)



# test_Karatsuba_mult(5)
def test_Karatsuba_mult(k):
    #set_random_seed(2)

    R = QQ[x]
    n = ZZ(2**k-1)
    f = R.random_element(n)
    g = R.random_element(n)

    vec_f = f.coefficients(sparse=False) # or .list()
    vec_g = g.coefficients(sparse=False)
    
    r = Karatsuba_mult(vec_f, vec_g, 2**k)
    print R(r) == f*g


def Karatsuba_mult(vec_f, vec_g, n):

    R = QQ[x]

    if (n == 1):
        return vec_f[0]*vec_g[0]

    A0 = vec_f[0:n/2]
    A1 = vec_f[n/2:]
    B0 = vec_g[0:n/2]
    B1 = vec_g[n/2:]
    
    # A_0 * B_0
    A0B0 = Karatsuba_mult(A0, B0, n/2)

    # A_1 * B_1    
    A1B1 = Karatsuba_mult(A1, B1, n/2)

    # (A_0 + A_1) * (B_0 + B_1)
    A0pA1 = (R(A0) + R(A1)).list()
    B0pB1 = (R(B0) + R(B1)).list()

    # fix vector
    while (len(A0pA1) < n):
        A0pA1.append(0)
    while (len(B0pB1) < n):
        B0pB1.append(0)
        
    u = Karatsuba_mult(A0pA1, B0pB1, n/2)
    diff = R(u) - R(A0B0) - R(A1B1)
    
    result = R(A1B1) * R(x**n) + diff * R(x**(n/2)) + R(A0B0)
    r = result.list()

    while (len(r) < 2*n):
        r.append(0)
        
    return r
    

# compare_timings_again (11)
def compare_timings_again (max_k):

    num_trials_each = 10
    
    R = QQ[x]
    time_classic = []
    time_Karatsuba = []
    
    for k in range(7, max_k, 1):
        n = 2**k-1
        time_c = 0
        time_K = 0
        print n
        for i in range(num_trials_each):

            f = R.random_element(n)
            g = R.random_element(n)
            vec_f = f.coefficients(sparse=False)
            vec_g = g.coefficients(sparse=False)

            # timing classic
            start = time.time()
            f._mul_generic(g)
            end = time.time()
            time_c = time_c + (end - start) 

            # timing Karatsuba           
            start = time.time()
            Karatsuba_mult(vec_f, vec_g, 2**k)
            end = time.time()
            time_K = time_K + (end - start) 

        time_c = RR(time_c / num_trials_each)
        time_K = RR(time_K / num_trials_each)
        
        time_classic.append(time_c)
        time_Karatsuba.append(time_K)


    return time_classic, time_Karatsuba

