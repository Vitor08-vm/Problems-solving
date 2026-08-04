def busca_binaria(marmores,inicio,fim,alvo):
    i = 0
    if fim >= inicio:
        i += 1
        meio = ((inicio + fim) // (2))
        if marmores[meio] == alvo:
            while marmores[meio-1] == alvo and meio > 0:
                meio -= 1
            return meio + 1
        
        elif marmores[meio] > alvo:
            return busca_binaria(marmores,inicio,meio-1,alvo)
        
        elif marmores[meio] < alvo:
            return busca_binaria(marmores,meio+1, fim, alvo)
    return False        


i = 0
while True:
    i += 1
    N, Q = map(int, input().split())
    
    if N == 0 and Q == 0:
        break
        
    marmores = []
    for _ in range(N):
        num = int(input())
        marmores.append(num)
        
    marmores.sort()
    print(f"CASE# {i}:")
    
    for _ in range(Q):
        x = int(input())
        posicao = busca_binaria(marmores, 0, len(marmores) - 1, x)
        
        if posicao:
            print(f"{x} found at {posicao}")
        else:
            print(f"{x} not found")