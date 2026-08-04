def mergesort(mess, inicio, fim):
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        mergesort(mess,inicio,meio)
        mergesort(mess,meio,fim)
        merge(mess,inicio,meio,fim)

def merge(mess,inicio,meio,fim):
    left = mess[inicio:meio]
    right = mess[meio:fim]
    e, d = 0, 0
    for k in range(inicio, fim):
        if e >= len(left):
            mess[k] = right[d]
            d += 1
        elif d >= len(right):
            mess[k] = left[e]
            e += 1
        elif len(right[d]) > len(left[e]):
            mess[k] = right[d]
            d += 1
        else:
            mess[k] = left[e]
            e += 1
    return mess

N = int(input())
i = 0 
while i < N:
    i += 1
    word = input().split(" ")
    mergesort(word,0,len(word))
    print(" ".join(word))