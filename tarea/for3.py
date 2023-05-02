#determine cuales son los múltiplos de 5 comprendidos entre 1 y N con el ciclo for
N = int(input("Introduce el valor de N: "))
for i in range(1, N+1):
    if i % 5 == 0:
        print(i)
