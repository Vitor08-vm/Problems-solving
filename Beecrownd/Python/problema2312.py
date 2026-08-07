def print_ordenado(paises):
    tamanho = len(paises)
    
    for k in range(tamanho):
        maior = k
        
        for j in range(k + 1, tamanho):
            atual = j
            
            nome_m, ouro_m, prata_m, bronze_m = paises[maior]
            nome_a, ouro_a, prata_a, bronze_a = paises[atual]
            cond1 = ouro_a > ouro_m
            cond2 = (ouro_a == ouro_m) and (prata_a > prata_m)
            cond3 = (ouro_a == ouro_m) and (prata_a == prata_m) and (bronze_a > bronze_m)
            cond4 = (ouro_a == ouro_m) and (prata_a == prata_m) and (bronze_a == bronze_m) and (nome_a < nome_m)
            
            if cond1 or cond2 or cond3 or cond4:
                maior = atual
        if maior != k:
            paises[maior], paises[k] = paises[k], paises[maior]
            
    return paises

N = int(input())
paises_lista = []

for _ in range(N):
    dados = input().split()
    nome = dados[0]
    ouro = int(dados[1])
    prata = int(dados[2])
    bronze = int(dados[3])
    
    paises_lista.append([nome, ouro, prata, bronze])
paises_ordenados = print_ordenado(paises_lista)

# Imprimimos o resultado formatado
for p in paises_ordenados:
    print(f"{p[0]} {p[1]} {p[2]} {p[3]}")