def percentual(letra, texto):
    cima = 0
    baixo = len(texto)
    for palavra in texto:
        for k in range(len(palavra)):
            if palavra[k] == letra:
                cima += 1
                break
            
    return f"{(cima/baixo)*100:.1f}"        
            
letra = input()
texto = input().split()
print(percentual(letra, texto))
