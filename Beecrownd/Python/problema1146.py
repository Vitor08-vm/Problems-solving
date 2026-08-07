while True:
    N = int(input())
    if N == 0:
        break
    for k in range(1,N+1):
        if k == N:
            print(k)
        else:
            print(k, end = " ")