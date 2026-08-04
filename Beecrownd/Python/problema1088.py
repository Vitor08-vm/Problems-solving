def mergesort(lista,inicio,fim):
    inv = 0
    if (fim - inicio) > 1:
        meio = (inicio + fim) // (2)
        inv += mergesort(lista,inicio,meio)
        inv += mergesort(lista,meio,fim)
        inv += merge(lista,inicio,meio,fim)
    
    return inv 

def merge(lista,inicio,meio,fim):
    
    c1 = 0
    left = lista[inicio:meio]
    right = lista[meio:fim]
    (e , d) = (0 , 0)
    for k in range(inicio, fim):
        
        if e >= len(left):
            lista[k] = right[d]
            d += 1
        
        elif d >= len(right):
            lista[k] = left[e]
            e += 1
        
        elif right[d] > left[e]:
            lista[k] = left[e]
            e += 1
        
        else:
            lista[k] = right[d]
            d += 1
            c1 += len(left) - e
    return c1        

while True:
    entrada = list(map(int, input().split()))
    if len(entrada) == 1 and entrada[0] == 0:
        break
    N = entrada[0]
    seq = entrada[1:]
    winner = mergesort(seq,0,len(seq))
    if winner % 2 == 0:
        print("Carlos")
    else:
        print("Marcelo")
