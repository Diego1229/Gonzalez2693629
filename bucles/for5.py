def es_perfecto(n): # 
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n

numero = int(input("Introduce un número: "))
if es_perfecto(numero):
    print(f"{numero} es un número perfecto")
else:
    print(f"{numero} no es un número perfecto")
