def qtd_quad(N):
    if N == 1:
        return 1  
    return N**2 + qtd_quad(N-1)
        
while True:
    N = int(input())
    if N == 0:
        break
    print(qtd_quad(N))