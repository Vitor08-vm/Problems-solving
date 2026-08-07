def corretor(txt_gago):
    palavras = []
    indices = []
    for k in range(len(txt_gago)):
        if txt_gago[k] == " ":
            indices.append(k)
    h = -1
    for ind in indices:
        palavras.append(txt_gago[h+1:ind])
        h = ind
    palavras.append(txt_gago[h+1:len(txt_gago)])
    palavra = ""
    txt_certo = []
    for j in range(len(palavras)):
        if len(palavras[j]) == 1:
            palavra = palavras[j][0:1]
            txt_certo.append(palavra)
        else:
            if palavras[j][0:2] == palavras[j][2:4]:
                if len(palavras[j]) == 2:
                    palavra = palavras[j][0:2]
                    txt_certo.append(palavra)
                else:    
                    palavra = palavras[j][0:2] + palavras[j][4:len(palavras[j])]
                    txt_certo.append(palavra)
            else:
                txt_certo.append(palavras[j])
    txt_certo = " ".join(txt_certo)            
    return txt_certo
    
txt_gago = input()
print(corretor(txt_gago))