def quadrado_cubo(atual,maximo):
    if atual == maximo:
        return f"{atual**1} {atual**2} {atual**3}"
    print(f"{atual**1} {atual**2} {atual**3}")
    return quadrado_cubo(atual+1, maximo)
    
N = int(input())
print(quadrado_cubo(1,N))