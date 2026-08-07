def soma_fatorial(N,M):
    def fatorial(X):
        if X == 0:
            return 1
        return X * fatorial(X-1)
    return fatorial(N) + fatorial(M)
    
while True:    
    try:
        M, N = map(int, input().split())
        print(soma_fatorial(N, M))
    except EOFError:
        break