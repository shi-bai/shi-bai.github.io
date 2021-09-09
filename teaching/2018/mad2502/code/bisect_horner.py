# some floating polynomial arithmetic

# a polynomial with a known root x = 5 due to constructoin!
def eval_poly_with_root_5(x):
    return (78*x**100 + 29*x**99 + 60*x**98 + 32*x**97 + 40*x**96 + \
                80*x**95 + 80*x**94 + 84*x**93 + 27*x**92 + 37*x**91 + \
                47*x**90 + 70*x**89 + 43*x**88 + 23*x**87 + 4*x**86 + \
                73*x**85 + 95*x**84 + 74*x**83 + 85*x**82 + 13*x**81 + \
                61*x**80 + 15*x**79 + 95*x**78 + 58*x**77 + 16*x**76 + \
                75*x**75 + 6*x**74 + 75*x**73 + 26*x**72 + 50*x**71 + \
                24*x**70 + 89*x**69 + 21*x**68 + 78*x**67 + 64*x**66 + \
                48*x**65 + 53*x**64 + 32*x**63 + 46*x**62 + 44*x**61 + \
                3*x**60 + 64*x**59 + 91*x**58 + 68*x**57 + 25*x**56 + \
                71*x**55 + 45*x**54 + 55*x**53 + 63*x**52 + 5*x**51 + \
                41*x**50 + 64*x**49 + 19*x**48 + 15*x**47 + 50*x**46 + \
                25*x**45 + 90*x**44 + 56*x**43 + 45*x**42 + 48*x**41 + \
                17*x**40 + 4*x**39 + 61*x**38 + 8*x**37 + 53*x**36 + \
                29*x**35 + 39*x**34 + 76*x**33 + 11*x**32 + 20*x**31 + \
                36*x**30 + 13*x**29 + 8*x**28 + 71*x**27 + 2*x**26 + \
                76*x**25 + 9*x**24 + 48*x**23 + 45*x**22 + 87*x**21 + \
                31*x**20 + 69*x**19 + 67*x**18 + 8*x**17 + 2*x**16 + \
                30*x**15 + 90*x**14 + 43*x**13 + 48*x**12 + 46*x**11 + \
                75*x**10 + 65*x**9 + 62*x**8 + 66*x**7 + 39*x**6 + \
                65*x**5 + 12*x**4 + 94*x**3 + 29*x**2 + 30*x + 64) * (x - 5)

# note after multiplication with (x-5) this polynomial is
# 78*x^101 - 361*x^100 - 85*x^99 - 268*x^98 - 120*x^97 - 120*x^96 - 320*x^95 - 316*x^94 - 393*x^93 - 98*x^92 - 138*x^91 - 165*x^90 - 307*x^89 - 192*x^88 - 111*x^87 + 53*x^86 - 270*x^85 - 401*x^84 - 285*x^83 - 412*x^82 - 4*x^81 - 290*x^80 + 20*x^79 - 417*x^78 - 274*x^77 - 5*x^76 - 369*x^75 + 45*x^74 - 349*x^73 - 80*x^72 - 226*x^71 - 31*x^70 - 424*x^69 - 27*x^68 - 326*x^67 - 272*x^66 - 187*x^65 - 233*x^64 - 114*x^63 - 186*x^62 - 217*x^61 + 49*x^60 - 229*x^59 - 387*x^58 - 315*x^57 - 54*x^56 - 310*x^55 - 170*x^54 - 212*x^53 - 310*x^52 + 16*x^51 - 141*x^50 - 301*x^49 - 80*x^48 - 25*x^47 - 225*x^46 - 35*x^45 - 394*x^44 - 235*x^43 - 177*x^42 - 223*x^41 - 81*x^40 + 41*x^39 - 297*x^38 + 13*x^37 - 236*x^36 - 106*x^35 - 119*x^34 - 369*x^33 - 35*x^32 - 64*x^31 - 167*x^30 - 57*x^29 + 31*x^28 - 353*x^27 + 66*x^26 - 371*x^25 + 3*x^24 - 195*x^23 - 138*x^22 - 404*x^21 - 86*x^20 - 278*x^19 - 327*x^18 - 38*x^17 + 20*x^16 - 60*x^15 - 407*x^14 - 167*x^13 - 194*x^12 - 155*x^11 - 310*x^10 - 263*x^9 - 244*x^8 - 291*x^7 - 130*x^6 - 313*x^5 + 34*x^4 - 441*x^3 - 115*x^2 - 86*x - 320

print(eval_poly_with_root_5(5))

# we need a list of above polynomial
List_poly5 = list((-320 ,  -86 ,  -115 ,  -441 ,  34 ,  -313 ,  -130 ,  -291 ,  -244 ,  -263 ,  -310 ,  -155 ,  -194 ,  -167 ,  -407 ,  -60 ,  20 ,  -38 ,  -327 ,  -278 ,  -86 ,  -404 ,  -138 ,  -195 ,  3 ,  -371 ,  66 ,  -353 ,  31 ,  -57 ,  -167 ,  -64 ,  -35 ,  -369 ,  -119 ,  -106 ,  -236 ,  13 ,  -297 ,  41 ,  -81 ,  -223 ,  -177 ,  -235 ,  -394 ,  -35 ,  -225 ,  -25 ,  -80 ,  -301 ,  -141 ,  16 ,  -310 ,  -212 ,  -170 ,  -310 ,  -54 ,  -315 ,  -387 ,  -229 ,  49 ,  -217 ,  -186 ,  -114 ,  -233 ,  -187 ,  -272 ,  -326 ,  -27 ,  -424 ,  -31 ,  -226 ,  -80 ,  -349 ,  45 ,  -369 ,  -5 ,  -274 ,  -417 ,  20 ,  -290 ,  -4 ,  -412 ,  -285 ,  -401 ,  -270 ,  53 ,  -111 ,  -192 ,  -307 ,  -165 ,  -138 ,  -98 ,  -393 ,  -316 ,  -320 ,  -120 ,  -120 ,  -268 ,  -85 ,  -361 ,  78))

print(List_poly5)


# again Horner's method (copied from previous lecture)
def Horner(L, x):
    value = 0
    n = len(L)
    for i in range(n):
        value = value * x + L[n-i-1]
    return value

print (Horner(List_poly5, 5))


# let's combine bisection with horner to find its root

#  bisection (copied from previous lecture)
def bisect_second(a, b):
    ''' Find root of a continuous function f.
    Note one should make sure f(a) * f(b) <= 0
    '''

    if (Horner(List_poly5, a) * Horner(List_poly5, b) > 0):
        return " input possibly wrong"

    num_steps = 0
    c = (a + b) / 2.0
    tolerance = 0.01
    while ( abs(Horner(List_poly5, c)) > tolerance ):
        # if they have oppo. sign
        if (Horner(List_poly5, a) * Horner(List_poly5, c) < 0):
            b = c
        # otherwise f(a)*f(c) > 0   
        else:
            a = c
        c = (a + b) / 2.0
        num_steps = num_steps + 1
        print ('# in current', num_steps, "guess, approx. root is ", c, "with error", abs(Horner(List_poly5, c)))
    print ('# after', num_steps, "guesses we approx. the root of the given polynomial is ", c)
    return


bisect_second(4.5, 5.2)

# outputs 
# in current 1 guess, approx. root is  5.025 with error 2.808854273955507e+70
# in current 2 guess, approx. root is  4.9375 with error 1.2151191159841145e+70
# in current 3 guess, approx. root is  4.98125 with error 8.797000623131238e+69
# in current 4 guess, approx. root is  5.003125000000001 with error 2.2710410664433652e+69
# in current 5 guess, approx. root is  4.9921875 with error 4.562974721887086e+69
# in current 6 guess, approx. root is  4.99765625 with error 1.5270515428234935e+69
# in current 7 guess, approx. root is  5.0003906250000005 with error 2.687974807244499e+68
# in current 8 guess, approx. root is  4.9990234375 with error 6.538911314131722e+68
# in current 9 guess, approx. root is  4.999707031250001 with error 1.9886437250904566e+68
# in current 10 guess, approx. root is  5.000048828125001 with error 3.337110377732368e+67
# in current 11 guess, approx. root is  4.999877929687501 with error 8.314347780255744e+67
# in current 12 guess, approx. root is  4.999963378906251 with error 2.4985649561151442e+67
# in current 13 guess, approx. root is  5.000006103515626 with error 4.167829948190956e+66
# in current 14 guess, approx. root is  4.999984741210939 with error 1.041513015334679e+67
# in current 15 guess, approx. root is  4.999995422363282 with error 3.1252056822545886e+66
# in current 16 guess, approx. root is  5.000000762939454 with error 5.2092317602548445e+65
# in current 17 guess, approx. root is  4.999998092651368 with error 1.3022384845572988e+66
# in current 18 guess, approx. root is  4.9999994277954105 with error 3.906819631231031e+65
# in current 19 guess, approx. root is  5.000000095367432 with error 6.511452933503623e+64
# in current 20 guess, approx. root is  4.999999761581421 with error 1.6278523668486214e+65
# in current 21 guess, approx. root is  4.999999928474427 with error 4.8835733479552583e+64
# in current 22 guess, approx. root is  5.00000001192093 with error 8.139303233041885e+63
# in current 23 guess, approx. root is  4.9999999701976785 with error 2.0348238876606598e+64
# in current 24 guess, approx. root is  4.999999991059305 with error 6.1044732948207224e+63
# in current 25 guess, approx. root is  5.000000001490117 with error 1.0174134680365688e+63
# in current 26 guess, approx. root is  4.9999999962747115 with error 2.543530222155638e+63
# in current 27 guess, approx. root is  4.999999998882414 with error 7.6305869353812705e+62
# in current 28 guess, approx. root is  5.000000000186265 with error 1.2717687916914392e+62
# in current 29 guess, approx. root is  4.99999999953434 with error 3.179409220268356e+62
# in current 30 guess, approx. root is  4.999999999860302 with error 9.538203277959359e+61
# in current 31 guess, approx. root is  5.000000000023284 with error 1.5897629122806456e+61
# in current 32 guess, approx. root is  4.999999999941792 with error 3.974267863112881e+61
# in current 33 guess, approx. root is  4.999999999982538 with error 1.1922496633173194e+61
# in current 34 guess, approx. root is  5.0000000000029114 with error 1.9878546206523423e+60
# in current 35 guess, approx. root is  4.999999999992725 with error 4.967330277189972e+60
# in current 36 guess, approx. root is  4.999999999997819 with error 1.4892703051986344e+60
# in current 37 guess, approx. root is  5.000000000000365 with error 2.492562097955577e+59
# in current 38 guess, approx. root is  4.999999999999092 with error 6.199518398748099e+59
# in current 39 guess, approx. root is  4.999999999999728 with error 1.8557311944833298e+59
# in current 40 guess, approx. root is  5.000000000000046 with error 3.1355933031785306e+58
# in current 41 guess, approx. root is  4.999999999999887 with error 7.711786286365786e+58
# in current 42 guess, approx. root is  4.999999999999966 with error 2.2890940914673878e+58
# in current 43 guess, approx. root is  5.000000000000006 with error 4.4477355067851204e+57
# in current 44 guess, approx. root is  4.999999999999986 with error 9.904589028648611e+57
# in current 45 guess, approx. root is  4.9999999999999964 with error 2.5029789234128994e+57
# in current 46 guess, approx. root is  5.000000000000002 with error 1.0275144006647089e+57
# in current 47 guess, approx. root is  4.999999999999999 with error 5.045564218616473e+56
# in current 48 guess, approx. root is  5.0 with error 0.0
# after 48 guesses we approx. the root of the given polynomial is  5.0
