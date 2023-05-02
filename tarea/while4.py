 
#  Determinar si un numero es o no es primo con el ciclo while
y = int(input("Ingrese un número: "))
x = 0
i = 1
while i <= y:
    if y % i == 0:
        x += 1
    i += 1

if x == 2:
    print(y, "es primo")
else:
    print(y, "no es primo")
