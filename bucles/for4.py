x=abs(int(input("digita un numero: ")))
div=0
nodivi=0
cont=0 
primo=0 

for i in range(1,x+1):
    if x%i==0:
        divi=i
        cont=+1
if cont<=2:
    primo=cont 
    print("el numero es primo")
else:
    print("el numero no es primo")
    print(f"se divide en {cont} numeros")





 