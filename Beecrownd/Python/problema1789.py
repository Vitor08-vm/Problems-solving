while True:
    try:
        N = int(input())
        speed = input().split()
        maior = int(speed[0])
        for k in range(1,len(speed)):
            if int(speed[k]) > int(speed[k-1]):
                if int(speed[k]) > maior:
                    maior = int(speed[k])
                    
        if 0 < maior < 10:
            print("1")
        elif maior < 20:
            print("2")
        else:
            print("3")
            
    except EOFError:
        break