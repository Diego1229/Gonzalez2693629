import random  #esta funcioncion contiene ralaciones gcon generacion de un numero aleatoreo
def llenalista(tamaño,rango): # esta moma un argumento tamaño y rango 
    tam=random.randint(15,tamaño) # genera un numero aleatoreo entre 15 y tamaño
    while tam==tam: # esta line crea un bucle 'while' que se ejecuta minetras el tamaño sea igual asi mismo 
        tam=random.randint(15,tam) # aqui se actualiza el valor del tamaño generando un nuevo numero aleatoreo entre 15 y el valor actuall de tam 
        if tam%5==0: # aqui se verefica el valor del tamaño si el resto de la división de tamaño entre 5 es igual a 0.
            lista =[round(random.uniform(1,50,rango),2) for i in range (tam)]# aqui se crea una lista por comprencion de lista, cada elemento de la lista es un numero aleatoreo generado utilizando random.uniform(1, 50, rango) el cual genera un numero flotante aleatoreo entre 1y 50 con rango cantidad de decimales. La función round() se utiliza para redondear cada número a 2 decimales   
            return lista  #esta lista  devuelve la lista generada 

def ordenAsen(lista):  #definimos la funcion toma una lista como argumento 
    for i in range(len(lista)): # este es un buble for se repite varias veces sobre los indices de la lista sobre 0 hasta la longitud de la lista menos 1. se le agrega la variable 'i' representa el indice actual 
        for j in range(i+1,len(lista)): #esta bucle for se repite varias veces sobre los indices de la lista desde i+1 hasta la longitud de la lista, la variable 'j' representa el indice actual y se inicia dede 'i+1' para comparar el elemento en la posicion 'i' con elementos restantes
         if lista[i]>lista[j]:# aqui se verifica si el elemento en la posicion 'i' de la lista es  mayor que el elemento de la posicion 'j'
             aux=lista[i]# en esta linea se asigna un valor en la posicision 'i' a la variable 'aux' esto es importante para cambiar los numeros de lugar 
             lista[i]=lista[j] # en la posicion j se asigna la posicion 'i' 
             lista[j]=aux #se almasena sen 'auxel elemento original en la posicion 'i' se asigna ala posicion 'j' completando asi el intercambio 
    return lista     

def quintiles(lista,valor): 
    quintiles=valor*len(lista)/5 #se calcula el valor de los quintiles multiplicando el parámetro valor por la longitud de la lista y dividiéndolo por 5  
    mayor=int(quintiles) #se convierte a un número entero utilizando la función int()
    menor=int(valor-1)*len(lista)/5 #Se calcula el valor del menor índice de la lista para el quintil. Se resta 1 del parámetro valor y se multiplica por la longitud de la lista, luego se divide por 5 
    if len(lista)>quintiles: #se verifica si la longitud de la lista esta mayor que el valor de los quintiles
        listaqui=list[menor:mayor] # Si es así, se crea una nueva lista listaqui que contiene los elementos de la lista original desde el índice menor hasta el índice mayor
        return listaqui
    else:
        return f"no se puede hallar el quintil" # no es mayor que quintiles, se devuelve un mensaje indicando que no se puede hallar el quintil.
    
lista1=llenalista(100,1.79)
division=len(lista1)/5
print(ordenAsen(lista1))
print(len(lista1))
x=abs(int(input("dijita que quintil quieres hallar: "))) 
print(quintiles(lista1,x))
