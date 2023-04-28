inicio = int(input("Ingrese el inicio de la serie: "))
fin = int(input("Ingrese el fin de la serie: "))
cantidad = int(input("Ingrese la cantidad a incrementar o decrementar: "))

serie = list(range(inicio, fin+1, cantidad)) #la fincion rangue se utiliza para generar la serie en forma de lista.
print("La serie resultante es:", serie)

num_positivo = int(input("Ingrese un número positivo que esté en la serie: "))
n = int(input("Ingrese el número 'n' para contar sus múltiplos: ")) # el usuario solicita un numero positivo que se encuentre en la serie y otro numero 'n'para encontrar sus multiplos.
multiplos_n = [i for i in serie if i % n == 0 and i <= num_positivo]
print("Hay", len(multiplos_n), "múltiplos de", n, "en la serie desde cero hasta", num_positivo, "y son:", multiplos_n)
