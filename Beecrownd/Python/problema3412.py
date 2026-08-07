def media(nota):
    if len(nota) <= 2:
        return f"{(sum(nota)/ 2):.1f}"
    elif len(nota) == 3:
        return f"{(sum(nota) / 3):.1f}"
    else:
        below = nota[0]
        for k in range(len(nota)-1):
            if nota[k] < below:
                below = nota[k]
        if below < nota[-1]:
            return f"{((sum(nota)-below) / 3):.1f}"
        else:
            return f"{((sum(nota)-nota[-1]) / 3):.1f}"


N = int(input())
i = 0
nome_media = []
while i < N:
    i += 1
    nome = input()
    nota = list(map(float, input().split()))
    nome_media.append(f"{nome}: {media(nota)}")
for res in nome_media:
    print(res)