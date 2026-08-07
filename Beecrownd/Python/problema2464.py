def mensagem(falsa,cripto):
    import string
    alfabeto = [letra for letra in string.ascii_lowercase[0:len(cripto)]]
    verdadeira = ""
    for letra in falsa:
        for j in range(len(cripto)):
            if letra == cripto[j]:
                verdadeira += alfabeto[j]
                break
    return verdadeira        

cripto = input()
falsa = input()
print(mensagem(falsa,cripto))