primeiro = True
while True:
    N = int(input())
    if N == 0:
        break
    if not primeiro:
        print()
    primeiro = False    
    camisa_nomes = {}
    pmeiro = []
    segundo = []
    terceiro = []
    quarto = []
    quinto = []
    sexto = []
    for _ in range(N):
        nome = input()
        cor, tam = input().split()
        if cor == "branco" and tam == "P":
            pmeiro.append(nome)
        elif cor == "branco" and tam == "M":
            segundo.append(nome)
        elif cor == "branco" and tam == "G":
            terceiro.append(nome)
        elif cor == "vermelho" and tam == "P":
            quarto.append(nome)
        elif cor == "vermelho" and tam == "M":
            quinto.append(nome)
        elif cor == "vermelho" and tam == "G":
            sexto.append(nome)
    pmeiro.sort()
    segundo.sort()
    terceiro.sort()
    quarto.sort()
    quinto.sort()
    sexto.sort()
    camisa_nomes.update({"branco P":pmeiro})
    camisa_nomes.update({"branco M":segundo})
    camisa_nomes.update({"branco G":terceiro})
    camisa_nomes.update({"vermelho P":quarto})
    camisa_nomes.update({"vermelho M":quinto})
    camisa_nomes.update({"vermelho G":sexto})
    for ch, lista in camisa_nomes.items():
        for k in range(len(lista)):
            print(f"{ch} {lista[k]}")