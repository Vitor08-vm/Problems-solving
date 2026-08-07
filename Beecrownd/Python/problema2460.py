def restantes(inicio,sairam):
    copia = inicio.copy()
    for k in range(len(inicio)):
        if inicio[k] in sairam:
            copia.remove(inicio[k])
    
    return " ".join(copia)        

N = int(input())
inicio = input().split()
M = int(input())
sairam = set(input().split())

print(restantes(inicio,sairam))