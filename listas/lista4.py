import random

n = int(input("ingresael tamaño de la lista "))
lista  = []

for i in range(n):
   lista.append(random.randint(1,100))
   
print("La lista original es:", lista)

suma = sum (lista)
print("el promedio de la suma es",suma)

promedio = suma / n
print("El promedio de la lista es:", promedio)

menor = min(lista) #se utiliza la funcion min() para encontrar el numero menor en la lista.
asendentes= sorted(lista) 
print("el numero menor de la lista es", menor)
print("lista ordena de manera ascendente", asendentes) 

descendentes= sorted(lista, reverse=True )
print("lista ordenada de una forma descendente", descendentes)

frecuencia= {}
for elemento in lista:
   if elemento in frecuencia:
       frecuencia[elemento] += 1
    
   else:
       frecuencia[elemento] =1

moda = max(frecuencia, key=frecuencia.get)
print("la moda de la lista es", moda)

numero= int(input("ingrese el numero que se desea buscar: " )) 
if numero in lista: 
    posicion = lista.index(numero)
    print("el numero", numero , " se encuentra en la posicion", posicion)
else:
     print("el numero", numero , "no se encuentra en la lista") 
    
num = int(input("¿Qué número desea buscar? "))
pos = -1
for i in range(n):
    if lista[i] == num:
        pos = i
        break 
    if pos != -1:
     print("El número", num, "se encuentra en la posición", pos, "de la lista.")
else:
     print("El número", num, "no se encuentra en la lista.")