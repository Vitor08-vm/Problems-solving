def formatNumber(X):
    if X % 10 == 0:
        return X//10
    return f"{X//10}.{X%10}"

for i in range(0,21,2):
    for j in range(10,31,10):
        print(f'I={formatNumber(i)} J={formatNumber(i + j)}')