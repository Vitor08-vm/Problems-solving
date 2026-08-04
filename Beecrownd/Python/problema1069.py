def diamonds(exp):
    store = 0
    qtd = 0
    for e in exp:
        if e == "<":
            store += 1
        elif e == ">" and store > 0:
            qtd += 1
            store -= 1
    return qtd        
    
N = int(input())
i = 0
while i < N:
    i += 1
    exp = input()
    print(diamonds(exp))