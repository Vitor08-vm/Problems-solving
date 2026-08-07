def menor(maior,count,r,soma):
    if soma > maior:
        return count
    return menor(maior,count+1,r+1,soma+r)

X = int(input())
Z = int(input())
while Z <= X:
    Z = int(input())
print(menor(Z,1,X+1,X)) 