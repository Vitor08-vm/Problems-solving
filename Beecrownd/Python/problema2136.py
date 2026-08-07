def vencedor(tudo):
    aux = []
    for nome, opcao in tudo.items():
        if opcao == "YES":
            aux.append(nome)
    maior_nome = aux[0] 
    for n in range(1,len(aux)):
        if len(aux[n]) >= len(aux[n-1]):
            if len(aux[n]) > len(maior_nome):
                maior_nome = aux[n]
    return maior_nome        
            
tudo = dict()
sohnome_Y = []
sohnome_N = []
i = True
while i:
    nome_opcao = input().split()
    if "FIM" in nome_opcao:
        i = False
    else:
        tudo.update({nome_opcao[0]:nome_opcao[1]})
        if nome_opcao[0] in tudo and nome_opcao[0] not in sohnome_Y:
            if tudo[nome_opcao[0]] == "YES":
                sohnome_Y.append(nome_opcao[0])
        if nome_opcao[0] in tudo and nome_opcao[0] not in sohnome_N:
            if tudo[nome_opcao[0]] == "NO":
                sohnome_N.append(nome_opcao[0])
sohnome_Y = sorted(sohnome_Y)
sohnome_N = sorted(sohnome_N)
c = len(sohnome_Y)
c1 = 0
for nome in sohnome_Y:
    print(nome)
for nome in sohnome_N:
    print(nome)
    
print()
print("Amigo do Habay:")
print(vencedor(tudo))