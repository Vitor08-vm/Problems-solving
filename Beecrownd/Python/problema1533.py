def mais_susp(random,ordem):
    for j in range(1,(len(random)+1)):
        if random[j-1] == ordem[1]:
            return j
t = True
while t:
    N = int(input())
    if N == 0:
        t = False
    else:
        random = list(input().split())
        for k in range(len(random)):
            random[k] = int(random[k])
        ordem = (sorted(random))[::-1]
        print(mais_susp(random,ordem))