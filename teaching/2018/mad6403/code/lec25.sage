def toyLLL_sizered (i, M, MO, MU):
    j = i-1
    while (j >= 0):
        muij = M[i]* MO[j] / (MO[j]*MO[j])
        if (abs(muij) > 0.5):
            cij = round(muij)
            M[i] =  M[i] - cij*M[j]
        j = j - 1
        


# M = sage.crypto.gen_lattice(m=10, seed=42)
# toyLLL(M)
def toyLLL (M, delta = 3/4, verbose = 1):
    m = M.nrows()
    n = M.ncols()

    i = 1
    while (i < m):
        # update Gram-schmidt basis
        MO,MU = M.gram_schmidt()
        
        # size reduce M[i]
        toyLLL_sizered (i, M, MO, MU)
        
        # updated MU (slow way)
        MO,MU = M.gram_schmidt()

        # Lovasz condition
        bi_star = MO[i].norm()^2
        bi1_star = MO[i-1].norm()^2
        muii1 = MU[i][i-1]^2

        if (bi_star < (delta-muii1)*bi1_star):
            M.swap_rows(i, i-1)
            i = max(i - 1, 1)
        else:
            i = i + 1

            
    # check if size-reduced and Lovasz condition
    if (verbose):
        print M.gram_schmidt()[1].numerical_approx()
        for i in range(0, m):
            print i, float(M[i].norm())

    return M

