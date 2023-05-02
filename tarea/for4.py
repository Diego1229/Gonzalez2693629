# Encuentre un número natural n más pequeño tal que la suma de los n primeros  números naturales (1 + 2 + 3 + 4…..) exceda de una cantidad (máximo) introducida por el teclado. Es decir cuantos números de la serie de los naturales debo sumar para superar el dato máximo.con el ciclo for
maximo = int(input("Introduce el número máximo a superar: "))
suma = 0
for i in range(1, maximo+1):
    suma += i
    if suma > maximo:
        print("La suma de los", i, "primeros números naturales supera el número máximo.")
        break
