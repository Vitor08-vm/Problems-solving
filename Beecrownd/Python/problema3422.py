def exchange(incident):
    if incident[1] == "1T":
        if int(incident[0]) <= 45:
            return int(incident[0])
        return f"45+{int(incident[0])-45}"
    else:
        if int(incident[0]) <= 45:
            return int(incident[0]) + 45
        return f"90+{int(incident[0])-45}"

N = int(input())
i = 0
while i < N:
    i += 1
    incident = input().split()
    print(exchange(incident))