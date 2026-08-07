def qtd(sequencia,n):
    qnts = 1
    if len(sequencia) >= 2:
        razao_i = sequencia[1] - sequencia[0]
        for k in range(2,len(sequencia)):
            razao_n = sequencia[k] - sequencia[k-1]
            if razao_n != razao_i:
                razao_i = razao_n
                qnts += 1
    else:
        return qnts
    return qnts        

n = int(input())
sequencia = list(map(int, input().split()))
print(qtd(sequencia,n))