N = int(input())
i = 0
while i < N:
    i += 1
    X, Y = map(int, input().split())
    soma = 0
    if X > Y:
        for k in range(Y+1, X):
            if k % 2 != 0:
                soma += k
    else:
        for j in range(X+1,Y):
            if j % 2 != 0:
                soma += j
    print(soma)            