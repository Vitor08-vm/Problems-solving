def controle(especiais, compradas):
    quantas = 0
    for k in range(len(especiais)):
        if especiais[k] not in compradas:
            quantas += 1
        else:
            continue
    return quantas    

N, C, M = map(int, input().split())
especiais = list(map(int, input().split()))
compradas = list(map(int, input().split()))
print(controle(especiais, compradas))