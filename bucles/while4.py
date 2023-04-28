while True:
    num1 = float(input("Ingresar el primer número: "))
    num2 = float(input("Ingresar el segundo número: "))
    if num1 > num2:
        break
    else:
        print("Error: el primer número debe ser mayor que el segundo. intente de nuevo .")

resultado = num1 - num2
if resultado > num2:
    resultado -= num2
    print("El resultado de la resta es:", resultado)
else:
    print("El resultado de la resta es:", resultado)
