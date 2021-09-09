import time

ii = CDF(I)
fpi = float(pi)

def dft(x):
    N = len(x)    
    result = []
    for l in range(N):
        r = 0
        for k in range(N):
            r = r + x[k] * exp((-2*fpi*ii/N)*k*l) # should use Horner
        result.append(r)

    return result
    

def fft(x):
    N = len(x)
    if N <= 1:
        return x

    # prepare r0 and r1
    r0 = []
    r1 = []
    for k in range(N//2):
        r0.append(x[k]+x[k+N//2])
        r1.append((x[k]-x[k+N//2])* exp(-(2*fpi*ii/N)*k))

    # call recursively fft on r0 and r1 at powers of w^2
    r0_w2 = fft(r0)
    r1_w2 = fft(r1)    

    # return result f(1), f(w), f(w^2), f(w^3) ...
    result = []
    for k in range(N//2):
        result.append(r0_w2[k])
        result.append(r1_w2[k])
        
    return result


# same as above but with w^-1
def ifft(x):
    N = len(x)
    if N <= 1:
        return x

    # prepare r0 and r1
    r0 = []
    r1 = []
    for k in range(N//2):
        r0.append(x[k]+x[k+N//2])
        r1.append((x[k]-x[k+N//2])* exp((2*fpi*ii/N)*k))

    # call recursively fft on r0 and r1 at powers of w^2
    r0_w2 = ifft(r0)
    r1_w2 = ifft(r1)    

    # return result f(1), f(w), f(w^2), f(w^3) ...
    result = []
    for k in range(N//2):
        result.append(r0_w2[k])
        result.append(r1_w2[k])
        
    return result


# test_fft(4)
def test_fft(k):
    #x = random_vector(2**k)
    #x = [1, 2, 3, 4, 5, 6, 7, 8]
    #x = [1, 2, 3, 4]
    x = [10, -2 + 2*I, -2, -2 - 2*I]        
    print "# x =      ", x
    print "# dft(x) = ", fft(x)
    #print "# fft(x) = ", fft(x)

    
# time_dft_fft(11)
def time_dft_fft(k_bound):

    time_dft = []
    time_fft = []
    
    for k in range(5, k_bound):
        print k
        x = random_vector(2**k)

        start = time.time()
        dft(x)        
        end = time.time()
        time_dft.append(end-start)

        start = time.time()
        fft(x)
        end = time.time()
        time_fft.append(end-start)

    return time_dft, time_fft


# coordinate wise product
def component_prod (a, b):
    l = []
    for i in range(len(a)):
        l.append(a[i]*b[i])
    return l


# an example
def test_prod ():
    f = [-1, -3, -2, 1, 0, -1]
    g = [-1, 0, 0, -2]
    for i in range(16-len(f)):
        f.append(0)
    for i in range(16-len(g)):
        g.append(0)
    print f
    print g
    
    f1 = fft(f)
    g1 = fft(g)
    fg1 = component_prod(f1, g1)
    fg = ifft(fg1)
    return fg
    
    
# variant
def fft2(x):
    N = len(x)
    if N <= 1:
        return x
    x_even = fft2(x[0:N+1:2])
    x_odd =  fft2(x[1:N+1:2])
    x_odd_w = [exp((-2*fpi*ii/N)*k)*x_odd[k] for k in range(N//2)]
    return [x_even[k] + x_odd_w[k] for k in range(N//2)] + [x_even[k] - x_odd_w[k] for k in range(N//2)]


