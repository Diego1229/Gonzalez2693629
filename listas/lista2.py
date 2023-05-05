import random #esta fincuion en ustilizada para generar numeros aleatoreos.
lista=[] 
tam=int(random.randint(10,20)) # esta funcion es un metodo que devuelve un elemento seleccionado de un numero entero del rango en especifico.
print(tam)
for i in range(tam): 
    num=int(random.randrange(100)) # con esta funcion se de vuelve un elemento seleccionado alatoriamente del rango especificado.
    lista.append(num) #con esta funcion se agrega un elemento al final de lista. 

print(lista)