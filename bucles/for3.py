num = int(input("Introduce un número entero: "))

print("Los divisores de", num, "son:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
