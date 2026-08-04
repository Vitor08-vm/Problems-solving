def wage(summary,dic):
    grana = 0
    for p1 in summary:
        if p1 in dic.keys():
            grana += dic[p1]
            
    return grana
    
    
M, N = map(int, input().split())
dic = {}

for _ in range(M):
    skill, money = input().split(" ")
    dic.update({skill:int(money)})
    
for k in range(N):
    salario = 0
    while True:
        try:
            linha = input().split(" ")
            if not linha:
                continue
            elif linha == ["."]:
                print(salario)
                break
            else:
                salario += wage(linha, dic)
        except EOFError:
            break