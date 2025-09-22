# Promedio y busqueda de eleemntos en un arreglo 
# diseña un programa en python que:
# 1- Permita declarar y crear un arreglo con calificaciones de un grupo de estudiantes (valores enteros del 0 al 100)
# 2- Calcule el promedio de las calificaciones de cada alumno y de las calificaciones almacenadas en el arreglo 
# 3.- Que permita buscar si una calificacion especifica (ingresada por el usuario) se encuentra en el arreglo 
# 4- Que muestre los resultados de forma clara en la pantalla 
b = int(input("Cuantos alumnos tienes?"))

for i in range(b):
    a = str(input("Ingresa el nombre de los alumnos: ")) 


m = int(input("¿Cuantas materias tienen los alumnos?"))
print (m)
c =  int(input("Ingresa las calificaciones de los alumnos: "))
print (c)

if c < 0 or c > 100:
    print ("No es valida la calificacion ingresada")

