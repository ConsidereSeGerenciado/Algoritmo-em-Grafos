import sys

def prim(matriz):
    S = [0] * len(matriz)
    v = 0
    custo = 0
    T = []
    S[v] = True
    u = 0
    while len(T) < len(matriz) - 1:
        menorPeso = sys.maxsize
        for i in range(len(matriz)):
            if S[i] != 0:
                for j in range(len(matriz)):
                    if not S[j] and matriz[i][j] != 0 and matriz[i][j] < menorPeso:
                        menorPeso = matriz[i][j]
                        u = i
                        v = j
        T.append((u, v))
        custo += menorPeso
        S[v] = True
    print(T, custo)

def kruskal(matriz):
    arestas = []
    ligacao = list(range(len(matriz)))
    posicao = [0] * len(matriz)
    T = []
    custo = 0
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] != 0:
                arestas.append((i, j, matriz[i][j]))
    arestas.sort(key=lambda x: x[2])
    for E in arestas:
        v, u, peso = E
        a = pai(ligacao, v)
        b = pai(ligacao, u)
        if a != b:
            T.append((v, u))
            custo += peso
            tabela(ligacao, posicao, a, b)
    print(T, custo)

def pai(ligacao, i): # igual como o professor mostrou o "a" e "b" em sala, que seriam usados para ajudar a unir na tabela
    if ligacao[i] == i:
        return i
    return pai(ligacao, ligacao[i])

def tabela(ligacao, posicao, a, b): # igual como o professor mostrou uma tabela em sala sobre quem tava ligado a quem
    aa = pai(ligacao, a)
    bb = pai(ligacao, b)
    if posicao[aa] < posicao[bb]:
        ligacao[aa] = bb
    elif posicao[aa] > posicao[bb]:
        ligacao[bb] = aa
    else:
        ligacao[bb] = aa
        posicao[aa] += 1

# kruskal([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])