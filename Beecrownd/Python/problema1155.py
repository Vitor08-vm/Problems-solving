def seq(i,n):
    n = 1/i
    if i == 1:
        return 1
    return n + (seq(i-1,n))

S = print(f"{seq(100,(1)/(100)):.2f}") 