def racional(op):
    operador = op[3]
    divid1 = int(op[0])
    divisor1 = int(op[2])
    divid2 = int(op[4])
    divisor2 = int(op[6])
    
    if operador == "+":
        cima = (divid1 * divisor2) + (divid2 * divisor1)
        baixo = divisor1*divisor2 
        main = f"{(cima)}/{(baixo)}"
        simple = f"{int(((cima)/mdc(cima,baixo)))}/{int(((baixo)/mdc(cima,baixo)))}" 
        return f"{main} = {simple}"
    elif operador == "-":
        cima = (divid1 * divisor2) - (divid2 * divisor1)
        baixo = divisor1*divisor2 
        main = f"{(cima)}/{(baixo)}"
        simple = f"{int(((cima)/mdc(cima,baixo)))}/{int(((baixo)/mdc(cima,baixo)))}" 
        return f"{main} = {simple}"
    elif operador == "*":
        cima = divid1 * divid2
        baixo = divisor1 * divisor2
        main = f"{(cima)}/{(baixo)}"
        simple = f"{int(((cima)/mdc(cima,baixo)))}/{int(((baixo)/mdc(cima,baixo)))}" 
        return f"{main} = {simple}"
    else:
        cima = divid1 * divisor2
        baixo = divisor1 * divid2
        main = f"{(cima)}/{(baixo)}"
        simple = f"{int(((cima)/mdc(cima,baixo)))}/{int(((baixo)/mdc(cima,baixo)))}" 
        return f"{main} = {simple}"
    
def mdc(num1, num2):
    atual = 0
    maior = 0
    if num1 >= num2:
        for k in range(2, num1+1):
            if num1 % k == 0 and num2 % k == 0:
                atual = k
                if atual > maior:
                    maior = atual
    else:
        for k in range(2, num2+1):
            if num1 % k == 0 and num2 % k == 0:
                atual = k
                if atual > maior:
                    maior = atual

    if maior == 0:
        return 1
    return maior                
    

while True:
    try:
        N = int(input())
        for _ in range(N):
            op = input().split()
            print(racional(op))
        
    except EOFError:
        break