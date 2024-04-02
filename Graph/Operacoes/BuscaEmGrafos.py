def BFS(listaAdj, v):
    Q = [v]
    analisado = []

    while Q:
        v = Q.pop(0)
        for j in listaAdj[v]:
            if j not in Q and j not in analisado:
                Q.append(j)
        analisado.append(v)
    for i in range(len(listaAdj)):
        if i not in analisado:
            analisado.append(i)

    return analisado


def DFS(listaAdj, v, analisado=None):
    if analisado is None:
        print(listaAdj)
        analisado = []
    analisado.append(v)  # adiciona o vértice visitado à lista de analisado
    for adj in listaAdj[v]:
        if adj not in analisado:
            # print(f"Adjacencia: {adj}")
            DFS(listaAdj, adj, analisado)
        # print(f"Pilha: {v}")
    if v == analisado[0]:  # verifica se vc está na primeira pilha que chamou as outras, ou seja, o primeiro "v"
        for i in listaAdj:
            if i not in analisado:
                DFS(listaAdj, i, analisado)
        return analisado


def DFSInterativo(listaAdj, v):
    pilha = []
    pilha.insert(0, v)
    analisado = []
    while pilha:
        # print(f"analisado: {analisado}")
        # print(f"Pilha: {pilha}")
        # print("---------------------------")
        v = pilha.pop(0)
        if v not in analisado:
            analisado.append(v)
        for j in reversed(listaAdj[v]):
            if j not in analisado:
                pilha.insert(0, j)
    for i in listaAdj:
        if i not in analisado:
            analisado.append(i)
            for k in listaAdj[i]:
                if k not in analisado:
                    analisado.append(k)
    return analisado
