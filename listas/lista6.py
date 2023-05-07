import random

n = int(input("¿Cuántos elementos desea en la lista? "))
lista = []

# Llenar la lista con números aleatorios
for i in range(n):
    lista.append(random.randint(1, 100))

print("La lista generada es:", lista)

# Calcular la suma de los números pares y el promedio de los números impares
suma_pares = 0
numeros_impares = []
suma_impares = 0
for numero in lista:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        numeros_impares.append(numero)
        suma_impares += numero

if len(numeros_impares) == 0:
    promedio_impares = 0
else:
    promedio_impares = suma_impares / len(numeros_impares)

print("La suma de los números pares es:", suma_pares)
print("El promedio de los números impares es:", promedio_impares)
