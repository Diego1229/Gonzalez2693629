from Book import *
from User import *
from Account import *


obj2 = Book ("La llorona" , "diego" , 102866 , "10/25/2014" , "diego")
obj1 = User ("diego" , 102866,obj2._obj_titulo)
obj3 = Account ("diego" , 102866,)


print(obj3.LibroReservado("diego","La llorona"))
print(obj3.LibroReservado("diego","La guerra de los cielos" ))
print(obj3.LibroDevuelto("diego","La llorona"))
print(obj3.LibroDevuelto("diego","La guerra de los cielos"))
print(obj3.LibroPerdido("diego"," La llorona"))
print(obj3.LibroPerdido("diego", "La Guerra de los cielos"))
print(obj3.LibroPerdido("diego", "La guerra de los cielos"))
print(obj3.LibroPerdido("diego", "La guerra de los cielos"))
print(obj3.calculate_fine())

obj1.CheckAccount("Harol" , obj3._obj_titulo["diego"])

obj2.AgregarBook()

# print(obj1.get_book_info ("La guerra de los cielos", obj2._informacion))
obj1.get_book_info ("La guerra de los cielos", obj2._informacion)