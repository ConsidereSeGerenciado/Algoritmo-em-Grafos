import numpy as np
def warshall(matriz):
    vertice = len(matriz)
    copiaMatriz = np.array(matriz)
    for k in range(0, vertice):
        for i in range(0, vertice):
            for j in range(0, vertice):
                if copiaMatriz[i][j] == 1 or (copiaMatriz[i][k] == 1 and copiaMatriz[k][j] == 1):
                    copiaMatriz[i][j] = 1
                else:
                    copiaMatriz[i][j] = copiaMatriz[i][j]
    return copiaMatriz

def caminhoEuleriano(matriz):
    vertice = len(matriz)
    total = 0
    soma = 0
    i = 0
    while (total <= 2) and (i < vertice):
        for j in range(vertice):
            soma += matriz[i][j]
        if soma % 2 != 0:
            total += 1
        i += 1
    if total >= 2:
        return False
    else:
        return True