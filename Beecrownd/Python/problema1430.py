def corretos(compassos):
    duracao = {
    'W':1.0, 'H':1/2, 'Q':1/4,
    'E':1/8, 'S':1/16, 'T':1/32,
    'X':1/64
    }
    alright = 0
    for c in compassos[1:-1]:
        soma = 0
        for nota in c:
            soma += duracao[nota]
        if soma == 1.0:
            alright += 1
    
    return alright        
    
while True:
    try:
        linha = input()
        if linha == "*":
            break
        compassos = linha.split("/")
        print(corretos(compassos))
    
    except EOFError:
        break