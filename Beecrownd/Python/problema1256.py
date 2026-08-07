def place(chaves,M,C):
    mod_lugar = {}
    for k in range(M):
        mod_lugar.update({str(k):[]})
    for ch in chaves:
        resto = str(ch % M)
        mod_lugar[resto].append(str((ch)))
    
    return mod_lugar
    
def print_ord(chaves):
    dic = place(chaves,M,C)
    for k,array in dic.items():
        if len(array) > 1:
            primeiro = True
            for j in range(len(array)):
                if primeiro:
                    print(f"{k} -> {array[j]} -> ", end = "")
                    primeiro = False
                
                elif j == len(array)-1:
                    print (f"{array[j]} -> \\")
                
                else:
                    print(f"{array[j]} -> ", end = "")
        
        elif len(array) == 1:
            print(f"{k} -> {array[0]} -> \\")
        
        else:
            print(f"{k} -> \\")
    
    return        


N = int(input())
for _ in range(N):
    M, C = map(int, input().split())
    chaves = list(map(int, input().split()))
    print_ord(chaves)
    if _ != N-1:
        print()
        