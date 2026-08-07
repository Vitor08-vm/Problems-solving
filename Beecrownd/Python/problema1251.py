import sys

def criar(txt):
    ja_foi = []
    caracteres_vistos = [] 
    
    for k in range(len(txt)):
        if txt[k] not in caracteres_vistos:
            rep = txt.count(txt[k])
            
            ja_foi.append([txt[k], rep])
            caracteres_vistos.append(txt[k])
            
    return ja_foi
    
def ordenado(ja_foi):
    for k in range(len(ja_foi)):
        escolhido = k
        for j in range(k+1, len(ja_foi)):
            if ja_foi[j][1] < ja_foi[escolhido][1]:
                escolhido = j
            elif ja_foi[j][1] == ja_foi[escolhido][1]:
                if ord(ja_foi[j][0]) > ord(ja_foi[escolhido][0]):
                    escolhido = j
                    
        if escolhido != k:
            ja_foi[escolhido], ja_foi[k] = ja_foi[k], ja_foi[escolhido]    
            
    return ja_foi            


def resolver():
    entrada = sys.stdin.read().splitlines()
    primeiro_caso = True
    
    for txt in entrada:
        if not txt: 
            continue 
        if not primeiro_caso:
            print()
        primeiro_caso = False
        
        matriz = criar(txt)
        pronta = ordenado(matriz)
        
        for linha in pronta:
            print(f"{ord(linha[0])} {linha[1]}")

if __name__ == '__main__':
    resolver()