def qtd(N, L, D):
    minima = (D * N) / (1000)
    razao = L
    while minima > L:
        L += razao
    return L    
    
N, L, D = map(int, input().split())
print(qtd(N, L, D))