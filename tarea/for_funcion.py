def primo (numero):
    
    if numero < 2:
        return False
    for  i in range(1,numero+1):
        if numero%i==0:
         ivi=i
         cont=+1
         return False
    return True


numero = int(input("ingrese un numero: "))
if primo(numero ):
    print(f"el {numero} es primo.")
else:
    print(f"{numero} no es primo.")

