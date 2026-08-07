def max(mapa):
    antes = 0
    depois = 0
    
    for k in range(len(mapa)):
        if k % 2 == 0:
            for j in range(0,len(mapa[k])):
                if mapa[k][j] == "o":
                    antes += 1
                elif mapa[k][j] == ".":
                    continue
                else:
                    if antes > depois:
                        depois = antes
                    antes = 0
                
        else:
            for j in range(len(mapa[k])-1,-1,-1):
                if mapa[k][j] == "o":
                    antes += 1
                elif mapa[k][j] == ".":
                    continue
                else:
                    if antes > depois:
                        depois = antes
                    antes = 0
    if antes > depois:             
        return antes
    else:
        return depois

N = int(input())
mapa = []
for _ in range(N):
    linha = input()
    mapa.append(linha)

print(max(mapa))      
    