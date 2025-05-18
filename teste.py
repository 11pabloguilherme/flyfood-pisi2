pontos = {}
matriz = []
caminhos = []


def achapontos(amatriz):
    for nl, li in enumerate(amatriz):
        for nc, co in enumerate(li):
            if co != '0':
                pontos[f'{co}'] = (nl, nc)


def achaopcoes(pontitos):
    if len(pontitos) == 0:
        return [[]]
    opcoes = []
    for a in range(len(pontitos)):
        pontodavez = pontitos[a]
        sobraram = pontitos[:a] + pontitos[a + 1:]
        for b in achaopcoes(sobraram):
            opcoes.append([pontodavez] + b)
    return opcoes


def caminhoscomr(pontitos):
    sopontos = list(pontitos.keys())
    sopontos.remove('R')
    todoscaminhos = achaopcoes(sopontos)
    for cada in todoscaminhos:
        completa = ['R'] + cada + ['R']
        caminhos.append(completa)


def calculadronometros(caminho, pontitos):
    dronometros = 0
    for i in range(len(caminho) - 1):
        pontopartida = pontitos[caminho[i]]
        pontochegada = pontitos[caminho[i+1]]
        dronometros += distancia(pontopartida, pontochegada)
    return dronometros


def distancia(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def escolhe(cami):
    menorcusto = 1000
    escolhido = []
    for i in cami:
        custoatual = calculadronometros(i, pontos)
        if custoatual < menorcusto:
            escolhido = i
            menorcusto = custoatual
    return escolhido


linhas = int(input('').split()[0])
for c in range(linhas):
    linha = (input('').split())
    matriz.append(linha)

achapontos(matriz)
caminhoscomr(pontos)
print(caminhos)
print(escolhe(caminhos))
