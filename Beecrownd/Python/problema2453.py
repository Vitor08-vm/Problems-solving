def decodificar(secreto):
    primeiro = True
    decodificada = ""
    for k in range(len(secreto)):
        if not primeiro:
            decodificada += " "
            for j in range(len(secreto[k])-1):
                if secreto[k][j] == "p":
                    if j % 2 == 0:
                        decodificada += secreto[k][j+1]
        else:
            primeiro = False
            for j in range(len(secreto[k])-1):
                if secreto[k][j] == "p":
                    if j % 2 == 0:
                        decodificada += secreto[k][j+1]
    return decodificada
    
secreto = input().split()
print(decodificar(secreto))