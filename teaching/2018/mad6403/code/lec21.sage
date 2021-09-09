def gs_mu_ij(ui, uj):
    return ui*uj / (uj*uj)

def gs_proj(ui, uj):
    return gs_mu_ij(ui, uj) * uj

# row matrix!
# B = random_matrix(ZZ, 10, 10, x = -100, y = 100)
# MO = gs(B)
def gs (B):
    MO = []
    for i in range(B.nrows()):
        bi = B[i]
        for j in range(len(MO)):
            bj = MO[j]
            proj_vec = gs_proj(B[i], bj)
            bi = bi - proj_vec
        MO.append(bi)
    MO = matrix(MO)
    return MO

