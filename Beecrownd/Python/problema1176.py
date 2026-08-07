def recursao(n,N,atras,atual):
    if n == N:
        return atras
    return recursao(n+1,N,atual,atras+atual) 
    
T = int(input())
i = 0
while i < T:
    i += 1
    N = int(input())
    print(f"Fib({N}) = {recursao(0,N,0,1)}")