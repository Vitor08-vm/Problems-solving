numeros= input().split()
soma = 0
for num in numeros[1:len(numeros)]:
    for i in range(int(num)):
        if i >= 0:
            soma += int(numeros[0]) + i
        else:
            continue
print(soma)    