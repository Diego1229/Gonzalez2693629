#Determin si un número es o no es perfecto. Un numero es perfecto si la suma de sus divisores sin incluir el propio 
# Pedimos al usuario que ingrese un número entero
num = int(input("Ingrese un número entero: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
         
if sum == num:
    print(num, "es un número perfecto")
else:
    print(num, "no es un número perfecto")

