def last_cor(L,C):
    if (C + L) % 2 == 0:
        return "1"
    else:
        return "0"
        
L = int(input())
C = int(input())
print(last_cor(L,C))