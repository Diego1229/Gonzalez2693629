numero = int(input("Introduce un número entero positivo: "))
divisor = 1

print("Los divisores de", numero, "son:")

while divisor <= numero:
    divisor += 1

def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

divisores = encontrar_divisores(numero)
print("Divisores de", numero, "encontrados con función:")
for divisor in divisores:
    print(divisor)
