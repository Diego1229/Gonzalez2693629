# Pedimos al usuario que ingrese un número
n = int(input("Ingrese un número: "))

sum = 0

i = 1
while i < n:
    if n % i == 0:
        sum += i
    i += i
if sum == n:
    print(n, "es un número perfecto")
else:
    print(n, "no es un número perfecto")
