import random

n = int(input("¿Cuántos elementos desea en la lista? "))
lista = []

# Llenar la lista con números aleatorios
for i in range(n):
    if i == 0:
        # El primer número es aleatorio entre 1 y 9
        lista.append(random.randint(1, 9))
    else:
        # Los siguientes números son aleatorios entre el número anterior y la siguiente decena
        anterior = lista[i-1]
        limite_superior = ((anterior // 20) + 1) * 10
        lista.append(random.randint(anterior - 1, limite_superior + 2))

print("La lista generada es:", lista)

