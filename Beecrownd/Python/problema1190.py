def s_ou_m(matriz,O):
    soma = 0
    for k in range(len(matriz)):
        for j in range(len(matriz[k])):
            if (k + j) > 11 and j > k:
                soma += matriz[k][j]
    if O == "S":
        return f"{soma:.1f}"
    return f"{(soma/30):.1f}"    

O = input()
matriz = []
for k in range(12):
    linha = []
    for j in range(12):
        num = float(input())
        linha.append(num)
    matriz.append(linha)    
print(s_ou_m(matriz,O))