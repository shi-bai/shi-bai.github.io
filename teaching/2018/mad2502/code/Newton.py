# root-finding by Newton's method

tolerance = 0.0000001

def f(x):
    return x**5 - 4*x**3 - x + 7


def f_derivative(x):
    return 5*x**4 - 12*x**2 - 1


# copied from bisection.py from a previous lecture
def bisect_second(a, b):
    if (f(a) * f(b) > 0):
        return " input possibly wrong"
    num_steps = 0
    c = (a + b) / 2.0
    while ( abs(f(c)) > tolerance ):
        if (f(a)*f(c) < 0):
            b = c
        else:
            a = c
        c = (a + b) / 2.0
        num_steps = num_steps + 1

    print ('# after', num_steps, "steps, approx. root is ", c)
    return


# attempts (for bisection)
for i in range(-10, 10, 1):
    print(i, f(i))

bisect_second(-3, 2) 

def f2(x):
    return x**2 - 6


def f2_derivative(x):
    return 2*x


# Newton's method
def Newton_method (x):
    ''' x is the initial guess;
        f and f_derivative is defined above '''
    initial = x
    num_steps = 0
    
    while (abs(f2(x)) > 0.1):
        x = x - f2(x) / f2_derivative(x)
        print(x, f2(x), f2(x) / f2_derivative(x))
        num_steps = num_steps + 1
        
    print ('# initial = ', initial, ' after', num_steps, "steps, approx. root is ", x)
    return

Newton_method (1)


Newton_method(-3)
Newton_method(2)
Newton_method(0)
# more trials 
for i in range(-10, 10, 1):
    Newton_method(i)



    
# now we want to try the larger example in the last lecture (there x=5 is a root).
# take the old list, how to find the derivative?
List_poly5 = list((-320 ,  -86 ,  -115 ,  -441 ,  34 ,  -313 ,  -130 ,  -291 ,  -244 ,  -263 ,  -310 ,  -155 ,  -194 ,  -167 ,  -407 ,  -60 ,  20 ,  -38 ,  -327 ,  -278 ,  -86 ,  -404 ,  -138 ,  -195 ,  3 ,  -371 ,  66 ,  -353 ,  31 ,  -57 ,  -167 ,  -64 ,  -35 ,  -369 ,  -119 ,  -106 ,  -236 ,  13 ,  -297 ,  41 ,  -81 ,  -223 ,  -177 ,  -235 ,  -394 ,  -35 ,  -225 ,  -25 ,  -80 ,  -301 ,  -141 ,  16 ,  -310 ,  -212 ,  -170 ,  -310 ,  -54 ,  -315 ,  -387 ,  -229 ,  49 ,  -217 ,  -186 ,  -114 ,  -233 ,  -187 ,  -272 ,  -326 ,  -27 ,  -424 ,  -31 ,  -226 ,  -80 ,  -349 ,  45 ,  -369 ,  -5 ,  -274 ,  -417 ,  20 ,  -290 ,  -4 ,  -412 ,  -285 ,  -401 ,  -270 ,  53 ,  -111 ,  -192 ,  -307 ,  -165 ,  -138 ,  -98 ,  -393 ,  -316 ,  -320 ,  -120 ,  -120 ,  -268 ,  -85 ,  -361 ,  78))
print(List_poly5)

# copied from previous lecture
def Horner(L, x):
    value = 0
    n = len(L)
    for i in range(n):
        value = value * x + L[n-i-1]
    return value


def derivative_poly (L):
    L_derivative = []
    for i in range(1, len(L), 1):
        tmp = L[i] * i
        L_derivative.append(tmp)
    return L_derivative

dx_List_poly5 = derivative_poly (List_poly5)
print(dx_List_poly5)


def Newton_method2 (L, dx_L, x):
    ''' x is the initial guess;
        L and dx_L are list repre. for polynomial and it's derivative '''
    initial = x
    num_steps = 0
    while (abs(Horner(L, x)) > tolerance):
        x = x - Horner(L, x) / Horner(dx_L, x)
        #print(x, Horner(L, x))
        num_steps = num_steps + 1
        
    print ('# [combined with horner] initial = ', initial, ' after', \
               num_steps, "steps, approx. root is ", x)
    return

# previously bisect_second(4.5, 5.2)
Newton_method2(List_poly5, dx_List_poly5, 5.2)

# note it also gives you another approximated root for the polynomial
Newton_method2(List_poly5, dx_List_poly5, 4.5)
