#[] {} ()
x=100
print('tipo de x',type(x)) #funcion devuelve el tipo del objeto especificado 
lista=[1,1.4,'sena',['a','b',],'soacha']
print(f'elemento {lista[4]}')
print(len(lista)) # esta funcion devuelve el numero de elementos en un objeto
print('tipo de lista',type(lista))
print('ultimo indice',lista[-1]) #

print(len(lista))
lista.append(20) #esta funcion añade un elemento al final de la lista
lista.append('python')
print(lista)
lista.insert(len(lista),'java')
print(lista) 
