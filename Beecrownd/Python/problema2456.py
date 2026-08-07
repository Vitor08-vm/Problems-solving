def tipo(sequencia):
    eh_C = True
    eh_D = True
    for k in range(1,len(sequencia)):
        if sequencia[k] > sequencia[k-1]:
            continue
        else:
            eh_C = False
            break
    for j in range(1,len(sequencia)):
        if sequencia[j] < sequencia[j-1]:
            continue
        else:
            eh_D = False
            break
    if eh_C:
        return "C"
    elif eh_D:
        return "D"
    else:
        return"N"
        
        
sequencia = list(map(int, input().split()))        
print(tipo(sequencia))