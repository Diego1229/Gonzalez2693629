import random

def llenarLista(tam,rango):     
    lista=[(random.randrange)(rango) for i in range(tam)]   # la función "llenarLista" genera una lista de números aleatorios del tamaño especificado y dentro del rango dado, utilizando la función "random.randrange"
    return lista

def sumaLista(lista):
    sum=0
    for x in lista: #se utiliza la función "sumaLista" recorre todos los elementos de la lista proporcionada y los suma uno por uno, devolviendo el resultado final de la suma como resultado de la función.
        sum+=x
    return sum

def compararSuma (lista1,lista2): # en esta linea de codigo se utiliza la función "compararSuma" calcula la suma de dos listas de números utilizando la función "sumaLista" y luego compara las sumas. Devuelve la mayor suma o un mensaje indicando que las sumas son iguales. 
    suma1=sumaLista(lista1)
    suma2=sumaLista(lista2)
    if suma1>suma2:       
        mayor=suma1
        return mayor
    elif suma2>suma1:
        mayor=suma2
        return mayor
    else:
        return f"La suma de los numeros son iguales"
    
def ordenAscen(lista):            #esta linea de codigo ordena una lista en orden acendente utilizando un algoritmo "selection sort" ordenamiento por seleccion  esta línea permite intercambiar los elementos de la lista cuando se encuentra un par desordenado durante el proceso de ordenamiento. Al finalizar la función, la lista estará ordenada en orden ascendente y se devuelve como resultado.    
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    return lista

def promedioConjunto(lista1,lista2):
    suma=0
    for x in lista1:
        suma+=x               # este codigo calcula el promedio de dos conjuntos de números representados por las listas "lista1" y "lista2",sumando todos los elementos en cada conjunto y dividiendo la suma total por la cantidad de elementos en ambos conjuntos combinados.
    for x in lista2:
        suma+=x
    promedio= suma/(len(lista1)+(len(lista2)))
    return promedio

def promedio(lista):
    suma=0
    for x in lista:
        suma+=x
    promedio= suma/(len(lista1))
    return promedio

def promedioLista(lista1,lista2):       #este codigo utiluza la a función "promedioLista" compara el promedio de una lista específica con el promedio conjunto de dos conjuntos de números. Devuelve un mensaje indicando si el promedio de la lista es mayor, menor o igual al promedio conjunto.
    promedioCon= promedioConjunto(lista1,lista2)
    promedio1= promedio(lista1)
    if promedio1>promedioCon:
        return f"El promedio esta por encima del promedio Conjunto"
    elif promedio1<promedioCon:
        return f"El promedio esta por debajo del promedio Conjunto"
    else:
        return f"El promedio es igual"
    
def pares (lista1,lista2): #este codigo utiliza las funcion "pares" cuenta la cantidad de números pares en dos listas diferentes y compara las cantidades. Devuelve un mensaje indicando la cantidad de números pares en la lista con más pares o que hay la misma cantidad en ambas listas.
    par1=0
    par2=0
    for i in lista1:
        if i%2==0:
            par1+=1
    for i in lista2:
        if i%2==0:
            par2+=1
    if par1>par2:
        return f"{par1} Hay mas numeros par en la lista 1"
    elif par2>par1:
        return f"{par2} Hay mas numeros par en la lista 2"
    else:
        return "Hay igual cantidad de pares en las dos listas"

def impares(lista1,lista2): # esta función "impares" cuenta la cantidad de números impares en dos listas diferentes y compara las cantidades. Devuelve un mensaje indicando la cantidad de números impares en la lista con más impares o que hay la misma cantidad en ambas listas.
    impar1=0
    impar2=0
    for i in lista1:
        if i%2!=0:
            impar1+=1
    for i in lista2:
        if i%2!=0:
            impar2+=1
    if impar1>impar2:
        return f"{impar1} Hay mas numeros impar en la lista 1"
    elif impar2>impar1:
        return f"{impar2} Hay mas numeros impar en la lista 2"
    else:
        return "Hay igual cantidad de impares en las dos listas"

def numMayor(lista1,lista2): # la funcion "numMayor" toma dos listas y luego encuentra un numero mayor en cada lista utilizando el metodo, ".pop(-1)" el que elimina y devuelve el ultuimp elemento de la lista, luego compara los dos numero mayores y si uno es mayor que el otro lo devuelve un mensaje que indica que los numeros son mayores son iguales  
    mayor1=lista1.pop(-1)
    mayor2=lista2.pop(-1)
    if mayor1>mayor2:
        return(mayor1)
    elif mayor2>mayor1:
        return(mayor2)        #esta función determina el número mayor entre los dos números mayores de las dos listas dadas.
    else: 
        return f"Los numero mayores son iguales"
    
def numMen(lista1,lista2):
    menor1=lista1.pop(0)
    menor2=lista2.pop(0)
    if menor1<menor2:
        return(menor1)
    elif menor2<menor1:
        return(menor2)
    else: 
        return f"Los numero menores son iguales"


lista1=llenarLista(15,25)
lista2=llenarLista(15,25)
ordenAscen(lista1)
ordenAscen(lista2)
print("1-Suma de cada lista")
print("2-Comparar las dos sumas")
print("3-Promedio Conjunto")
print("4-Promedio de cada lista")
print("5-Comparar el promedio de las dos listas")
print("6-Impar de los listas")
print("7-Par de los listas")
print("8-Numero mayor de las dos listas")
print("9-Numero menor de las dos listas")
selector=1
while selector!=0:                                                  #este código crea un menu que permite al usuario seleccionar diferentes opciones para realizar diversas operaciones en las listas lista1 y lista2. El bucle while se ejecuta hasta que el usuario ingrese 0 para salir del programa.     
    selector=input("Digite la opcion: ")
    match selector:
        case "1":
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print("Suma de la lista 1",sumaLista(lista1))
            print("Suma de la lista 2",sumaLista(lista2))
        case "2":
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print("La suma mayor de la lista es: ",compararSuma(lista1,lista2))
        case "3":
            print("Promedio de las dos lista",promedioConjunto(lista1,lista2))
        case "4":
            print("Promedio de la lista 1",promedio(lista1))
            print("Promedio de la lista 2",promedio(lista2))
        case "5":
            print(promedioLista(lista1,lista2))
            print(promedioLista(lista2,lista1))
        case "6":
            print(impares(lista1,lista2))
        case "7":
            print(pares(lista1,lista2))
        case "8":
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print(numMayor(lista1,lista2))
        case "9":
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print(numMen(lista1,lista2))
        case "0":
            break