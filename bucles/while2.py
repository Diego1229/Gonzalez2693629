maximo = int(input("Introduce el máximo a superar: "))
suma = 0
i = 1

while suma < maximo:
    suma += i
    i += 1

print("El número natural n más pequeño para superar el máximo es:", i-1)
