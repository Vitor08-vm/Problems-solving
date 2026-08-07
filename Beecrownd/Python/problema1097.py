p = 7
for i in range(1,10,2):
    for j in range(p,17):
        atual = j
        for _ in range(3):
            print(f"I={i} J={atual}")
            atual -= 1
        p += 2
        break