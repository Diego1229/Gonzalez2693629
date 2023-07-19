def  solucion_ecuacion():
   
    try:
   
        a = float(input("Ingrese el valor de a: "))
        if a == 0:
            raise ZeroDivisionError("El coeficiente cuadrático (a) no puede ser cero.")

        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))

       

        deter = (b**2) - (4*a*c)
        if deter < 0:
            raise ValueError("la ecuacion no tiene soluciones reales")
       
        x1 = (-b + (deter)**(1/2))/(2*a)
        x2 = (-b - (deter)**(1/2))/(2*a)
 
        print(f"El valor de x1 es: {x1}")
        print(f"El valor de x2 es: {x2}")

    except ValueError:
        print("Error, caracter incorrecto.")
        
solucion_ecuacion()
