def parentese(expressao):
    contador = 0
    for char in expressao:
        if char == "(":
            contador += 1
        elif char == ")":
            contador -= 1
        
        if contador < 0:
            return "incorrect"
        
    if contador == 0:
        return "correct"
    else:
        return "incorrect"

while True:
    try:
        N = input()
        print(parentese(N))
    except EOFError:
        break