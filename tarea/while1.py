# Determine cuales son los múltiplos de 5 comprendidos entre 1 y N
N = int(input("Ingrese un valor para N: "))
i = 1
while i <= N:
    if i % 5 == 0:
        print(i)
    i += 1
