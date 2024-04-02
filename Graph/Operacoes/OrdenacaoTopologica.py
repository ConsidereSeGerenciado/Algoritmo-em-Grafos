def temposVertices(listaAdj, v):
    analisado = []
    tempoD = {}
    tempoT = {}
    tempoVertice = {}
    tempo = [0]

    def DFSTempo(listaAdj, v, tempo):
        tempo[0] += 1
        tempoD[v] = tempo[0]
        analisado.append(v)  # adiciona o vértice visitado à lista de analisado
        for adj in listaAdj[v]:
            if adj not in analisado:
                DFSTempo(listaAdj, adj, tempo)
        tempo[0] += 1
        tempoT[v] = tempo[0]

        if v == analisado[0]:  # verifica se vc está na primeira pilha que chamou as outras, ou seja, o primeiro "v"
            tempoT[v] = tempo[0]
            for adj in listaAdj:
                if adj not in analisado:
                    DFSTempo(listaAdj, adj, tempo)
            for i in listaAdj:
                tempoVertice[i] = f"{tempoD[i]}/{tempoT[i]}"
            return tempoVertice

    DFSTempo(listaAdj, v, tempo)
    return tempoVertice

def classificaArestas(listaAdj, v):
    cor = ['Branco'] * len(listaAdj)
    tipoAresta = [[None] * len(listaAdj) for _ in range(len(listaAdj))]
    tempoD = {}
    tempoT = {}
    tempo = [0]
    if cor[v] == 'Branco':
            visitaDFS(listaAdj, v, cor, tipoAresta, tempoD, tempoT, tempo)
    for adj in listaAdj:
        if cor[adj] == 'Branco':
            visitaDFS(listaAdj, adj, cor, tipoAresta, tempoD, tempoT, tempo)

def visitaDFS(listaAdj, v, cor, tipoAresta, tempoD, tempoT, tempo):
    cor[v] = 'Cinza'
    tempo[0] += 1
    tempoD[v] = tempo[0] + 1
    for adj in listaAdj[v]:
        if cor[adj] == 'Branco':
            tipoAresta[v][adj] = 'Tree'
            print(f"{v} {adj} {tipoAresta[v][adj]}")
            visitaDFS(listaAdj, adj, cor, tipoAresta, tempoD, tempoT, tempo)
        elif cor[adj] == 'Cinza':
            tipoAresta[v][adj] = 'Back'
            print(f"{v} {adj} {tipoAresta[v][adj]}")
        else:
            if tempoD[v] < tempoD[adj]:
                tipoAresta[v][adj] = 'Forward'
                print(f"{v} {adj} {tipoAresta[v][adj]}")
            else:
                tipoAresta[v][adj] = 'Cross'
                print(f"{v} {adj} {tipoAresta[v][adj]}")
    cor[v] = 'Preto'
    tempoT[v] = tempo[0] + 1

def verrificaDAG(listaAdj):
    cor = ['Branco'] * len(listaAdj)
    tipoAresta = [[None] * len(listaAdj) for _ in range(len(listaAdj))]
    tempoD = {}
    tempoT = {}
    i = 0
    tempo = [0]
    for adj in listaAdj:
        if cor[adj] == 'Branco':
            i = visitaDAG(listaAdj, adj, cor, tipoAresta, tempoD, tempoT, tempo)
    if i == 10:
        return 10
    else:
        return 1

def visitaDAG(listaAdj, v, cor, tipoAresta, tempoD, tempoT, tempo):
    cor[v] = 'Cinza'
    tempo[0] += 1
    tempoD[v] = tempo[0] + 1
    for adj in listaAdj[v]:
        if cor[adj] == 'Branco':
            tipoAresta[v][adj] = 'Tree'
            visitaDAG(listaAdj, adj, cor, tipoAresta, tempoD, tempoT, tempo)
        elif cor[adj] == 'Cinza':
            tipoAresta[v][adj] = 'Back'
            return 10
        else:
            if tempoD[v] < tempoD[adj]:
                tipoAresta[v][adj] = 'Forward'
            else:
                tipoAresta[v][adj] = 'Cross'
    cor[v] = 'Preto'
    tempoT[v] = tempo[0] + 1

def verificaDAG(listaAdj):
    if verrificaDAG(listaAdj) == 10:
        print("NÃO DAG")
    else:
        print("DAG")

def ordenacaoTopologica(listaAdj):
    L = []
    cor = ['branco'] * len(listaAdj)
    tipoAresta = [[None] * len(listaAdj) for _ in range(len(listaAdj))]
    tempoD = {}
    tempoT = {}
    tempo = [0]
    for adj in listaAdj:
        if cor[adj] == 'branco':
            visitaDFSTopologica(listaAdj, adj, cor, tipoAresta, tempoD, tempoT, tempo, L)
    print(L)

def visitaDFSTopologica(listaAdj, v, cor, tipoAresta, tempoD, tempoT, tempo, L):
    cor[v] = 'Cinza'
    tempo[0] += 1
    tempoD[v] = tempo[0] + 1
    for adj in listaAdj[v]:
        if cor[adj] == 'Branco':
            tipoAresta[v][adj] = 'Tree'
            visitaDFSTopologica(listaAdj, adj, cor, tipoAresta, tempoD, tempoT, tempo, L)
        elif cor[adj] == 'Cinza':
            tipoAresta[v][adj] = 'Back'
        else:
            if tempoD[v] < tempoD[adj]:
                tipoAresta[v][adj] = 'Forward'
            else:
                tipoAresta[v][adj] = 'Cross'
    cor[v] = 'Preto'
    tempoT[v] = tempo[0] + 1
    L.insert(0, v)