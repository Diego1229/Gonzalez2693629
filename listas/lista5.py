import random

def es_primo(n):
    if num <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("¿Cuántos elementos desea en la lista? "))
lista = []

for i in range(n):
    lista.append(random.randint(1, 100))
print("La lista es:", lista)


primos = []
for num in lista:
    if es_primo(num):
        primos.append(num)

if len(primos) == 0:
    print("No se encontraron números primos en la lista.")
else:
    print("Se encontraron", len(primos), "números primos en la lista:")
    print(primos)
