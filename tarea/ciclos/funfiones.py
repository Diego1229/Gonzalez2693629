import random
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)
l1=llenarLista(3,10)

def mayor_menor (lista):
    mayor = lista[0]
    menor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    return mayor, menor
mayor, menor = mayor_menor(l1)

def calcular_media(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    media = suma / len(lista)
    return media

media = calcular_media(l1)

def calcular_moda(lista):
    # Crear un diccionario para contar la frecuencia de cada valor en la lista
    frecuencias = {}
    for valor in lista:
        if valor in frecuencias:
            frecuencias[valor] += 1
        else:
            frecuencias[valor] = 1

    # Encontrar el valor con la frecuencia máxima
    moda = lista
    max_frecuencia = 0
    for valor, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            moda = valor
            max_frecuencia = frecuencia

    return moda

moda=calcular_moda(l1)

print(l1)
print("la suma de la lista",sumaLista(l1))
print("el promedio es",round(promedioLista(l1),2))
print("el valor maximo es",mayor)
print("el valor minimo",menor)
print("La media de la lista es:", media)
print("La moda de la lista", l1, "es:", calcular_moda(l1))
