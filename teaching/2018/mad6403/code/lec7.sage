mods = [11, 13, 17, 19]
vs = [2, 7, 1, 0]

def crt_ZZ (mods, vs):
    result = 0
    prod = 1
    for i in range(len(mods)):
        prod = prod * mods[i]
    print prod
    
    for i in range(len(mods)):
        m_i = mods[i]
        v_i = vs[i]
        a = ZZ(prod / m_i)
        b = m_i
        r, x, y = xgcd(a, b)
        result = result + x * a * v_i
        
    for i in range(len(mods)):
        print " # check ", result % mods[i]
        
    return
 
