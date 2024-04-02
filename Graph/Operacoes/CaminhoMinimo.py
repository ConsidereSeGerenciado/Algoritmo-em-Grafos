import sys


def dijkstra(matriz, vOrigem, vDestino):
    custo = [float('inf')] * len(matriz)
    rota = [0] * len(matriz)
    custo[vOrigem] = 0
    F = []
    N = set(range(len(matriz)))
    while N:
        v = min(N, key=lambda v: custo[v])
        if v == vDestino:
            break
        F.append(v)
        N.remove(v)
        for u in range(len(matriz)):
            if matriz[v][u] != 0 and custo[v] + matriz[v][u] < custo[u]:
                custo[u] = custo[v] + matriz[v][u]
                rota[u] = v

    verdadeiraRota = [vDestino]
    verticeAtual = vDestino
    while verticeAtual != vOrigem:
        verticeAtual = rota[verticeAtual]
        verdadeiraRota.insert(0, verticeAtual)

    diferencaCusto = custo[vDestino] - custo[vOrigem]

    return print(verdadeiraRota, diferencaCusto)


def encontrar_vertice_minimo(distancias, visitados):
    min_distancia = sys.maxsize
    min_vertice = -1

    for v in range(len(distancias)):
        if not visitados[v] and distancias[v] < min_distancia:
            min_distancia = distancias[v]
            min_vertice = v

    return min_vertice


def construir_caminho(rota, vOrigem, vDestino):
    caminho = []
    vertice = vDestino
    while vertice != vOrigem:
        caminho.append(vertice)
        vertice = rota[vertice]
    caminho.append(vOrigem)
    caminho.reverse()
    return caminho


def bellmanFord(matriz, vOrigem, vDestino):
    custo = [float('inf')] * len(matriz)
    rota = [0] * len(matriz)
    custo[vOrigem] = 0

    for i in range(len(matriz)):
        for u in range(len(matriz)):
            for v in range(len(matriz)):
                if matriz[v][u] != -1 and custo[v] + matriz[v][u] < custo[u]:
                    custo[u] = custo[v] + matriz[v][u]
                    rota[u] = v

    # for i in range(len(matriz)):
    #     for u in range(len(matriz)):
    #         if custo[u] > custo[i] + matriz[i][u]:
    #             return False

    verdadeiraRota = [vDestino]
    verticeAtual = vDestino
    while verticeAtual != vOrigem:
        verticeAtual = rota[verticeAtual]
        verdadeiraRota.insert(0, verticeAtual)
    print(f"{verdadeiraRota} {custo[vDestino] - custo[vOrigem]}")


def floydWarshall(matriz):
    n = len(matriz)
    d = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matriz[i][j] != -1:
                d[i][j] = matriz[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] != float('inf') and d[k][j] != float('inf'):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    print(d)


dijkstra([[0, 3, 8, 4, 0, 10], [3, 0, 0, 6, 0, 0], [8, 0, 0, 0, 7, 0], [4, 6, 0, 0, 1, 3], [0, 0, 7, 1, 0, 1],
          [10, 0, 0, 3, 1, 0]], 5, 0)

# floydWarshall([[0, 3, 8, -1, -4], [-1, 0, -1, 1, 7], [-1, 4, 0, -1, -1], [2, -1, -5, 0, -1], [-1, -1, -1, 6, 0]])
