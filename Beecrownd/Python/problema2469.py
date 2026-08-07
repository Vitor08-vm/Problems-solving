def moda(notas):
    maior = 0
    mais = 0
    for j in range(len(notas)):
        qtd = 0
        for k in range(j, len(notas)):
            if notas[k] == notas[j]:
                qtd += 1
        if qtd >= mais:
            mais = qtd
            maior = notas[j]
    return maior        

N = int(input())
notas = sorted(map(int, input().split()))
print(moda(notas))