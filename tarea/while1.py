numero = int(input("Introduce un número entero positivo: "))
divisor = 1

print("Los divisores de", numero, "son:")

while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
    divisor += 1

