T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    dicionario = {}
    
    for _ in range((M)):
        japones = input()
        portugues = input()
        dicionario.update({japones:portugues})
    
    traducao = []
    for k in range(N):
        linha = input()
        if not linha:
            continue
        else:
            linha = linha.split(" ")
            lista = []
            for palavra in linha:
                if palavra in dicionario.keys():
                    lista.append(dicionario[palavra])
                else:
                    lista.append(palavra)
            traducao.append(lista)        
    for p in traducao:
        print(" ".join(p))
    print()