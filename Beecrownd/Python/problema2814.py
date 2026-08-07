from math import floor
def perda_sonora(mapa, K):
    for k in range(len(mapa)):
        achei_J = mapa[k].find("J")
        if achei_J != -1:
            coluna_j = k
            break
    for w in range(len(mapa)):
        achei_F = mapa[w].find("F")
        if achei_F != -1:
            coluna_f = w 
            break
    altura = abs(coluna_f-coluna_j)
    base = abs(achei_J-achei_F)
    distancia = int(((altura**2 + base**2 )**0.5) * 10)
    maximo = floor((K) / (0.99**((distancia))))
    return maximo 
    
N = int(input())
i = 0
while i < N:
    mapa = []
    i += 1
    K, J = map(int, input().split())
    for _ in range(J):
        linha = input()
        mapa.append(linha)
    print(f"{perda_sonora(mapa, K)} dBs")   