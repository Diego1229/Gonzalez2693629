def restar(num1,num2):
    resultado = num1 - num2
    return resultado 
    
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
  
while num1 <= num2:      

    print("El primer número debe ser mayor que el segundo. Intente de nuevo.")
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))

resultado = restar(num1, num2)
print("El resultado de la resta es:", resultado)
