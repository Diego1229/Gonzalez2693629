
def solucion_ecuacion():

    try:   
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
    
        x1 = (-b + ((b**2) - (4*a*c))**(1/2))/(2*a)   
        x2 = (-b - ((b**2) - (4*a*c))**(1/2))/(2*a)
    
        print(f"el  valor de x1 es: {x1}")
        print(f"el valor de x2 es {x1}")
    
    except ValueError:
        print("error en el coeficiente")  
    
    except ZeroDivisionError as e:
        print(f"error: {e}")


solucion_ecuacion()  
