def dist_manhattan(tupleA, tupleB):
    dist = abs(tupleA[0]-tupleB[0]) + abs(tupleA[1]-tupleB[1])
    return dist

def encontrar_pontos(matriz):# encontrar pontos de interesse
    loc_pontos = {}
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            valor = matriz[i][j]
            if valor != 0:
                loc_pontos[valor] = (i, j)
    return loc_pontos

pontos = encontrar_pontos([[0, 0, 0, 0, 'D', 0, 0, 0, 0], 
                        [0, 'A', 0, 0, 0, 0, 0, 'E', 0], 
                        [0, 0, 0, 0, 'C', 0, 0, 0, 0], 
                        ['R', 0, 'B', 0, 0, 0, 0, 'F', 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 'H', 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        ['G', 0, 0, 0, 0, 0, 0, 0, 0]])

print(pontos)

def pontos_str(loc_pontos):
    juntar = []
    for i in loc_pontos:
        if i == 'R':
            continue
        juntar.append(i)
    return ''.join(juntar)

pontos_strr = pontos_str(pontos)

def permutacoes(pontos):
    if len(pontos) == 0:
        return [pontos]
    resultado = []
    for i in range(len(pontos)):
        atual = pontos[i]
        restante = pontos[:i] + pontos[i+1:]
        for p in permutacoes(restante):
            resultado.append(atual + p)
    return resultado

pontos_perm = permutacoes(pontos_strr)

rotas = ['R'+ p + 'R' for p in pontos_perm]

def calcular_distancias(loc_pontos, rotas): #calcular as distancias do ponto de partida ate os outros pontos(R-a-b-c-d-R)
    distancias = []
    for rota in rotas:
        soma = 0
        for i in range(len(rota) - 1):
            partida = loc_pontos[rota[i]]
            destino = loc_pontos[rota[i+1]]
            soma = soma + dist_manhattan(partida, destino)
        distancias.append((rota, soma))
    return distancias

distancia = calcular_distancias(pontos, rotas)
print(distancia)

def melhor_rota(distancia):
    menor_dist = distancia[0][1]
    melhor = distancia[0][0]
    for i in distancia[1:]:
        if i[1] <= menor_dist:
            melhor, menor_dist = i
    return melhor

melhor_percurso = melhor_rota(distancia)

def retirar_rs(melhor_rota):
    return melhor_rota[1:-1]

print(retirar_rs(melhor_percurso))
