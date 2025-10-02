#Implemente en python un programa que realice lo siguiente 
# 1. Cree un arreglo con las calificaciones de diez estudiantes considerando valores enteroes entre 0 y 10 
# 2. Al inicio se preguntara cuantas materias y alumnos estan en el curso 
# 3. Muestre en pantalla a los alumnos y todas las calificaciones 
# 4. Calcule y muestre promedio de las calificaciones por alumno y grupal 
# 5. Promedio de calificaciones por materia 
# 6. La calificacion minima y la maxima 
# 7. El numero de estudiantes que aprobaron (mayor o igual a 7) y los que reprobaron (menor a 7)
# 8. Permita al usuario buscar una calificacion especifica en el arreglo e indique si se encuentra o no 
# 9. Despues de la busqueda ordene el arreglo de mayor a menor y muestre el resultado en pantalla 

# Pedimos el número de alumnos
b = 10
# Guardamos los nombres en una lista
nombres = []

for i in range(b):
    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
    nombres.append(nombre)

# Pedimos el número de materias
m = int(input("¿Cuántas materias tienen los alumnos? "))

# Creamos un arreglo para calificaciones
calificaciones = []

for i in range(b):
    print(f"\nAlumno: {nombres[i]}")
    notas = []
    for j in range(m):
        cal = int(input(f"  Calificación {j+1}: "))
        # Validamos que la calificación esté entre 0 y 100
        if cal < 0 or cal > 10:
            print("Calificación no válida, se pondrá 0")
            cal = 0
        notas.append(cal)
    calificaciones.append(notas)

print("Promedio por Alumno")
for i in range(b):
    promedio_alumno = sum(calificaciones[i]) / m
    promedios_alumnos = []
    promedio_alumno = sum(calificaciones[i]) / m
    promedios_alumnos.append(promedio_alumno)
    print(f"{nombres[i]}: {promedio_alumno:.2f}")


todas = [nota for sublista in calificaciones for nota in sublista]
promedio_grupo = sum(todas) / len(todas)
print(f"\nPromedio general del grupo: {promedio_grupo:.2f}")

promedio_min = min(promedio_alumno)
promedio_max = max(promedio_alumno)
indice_min = nombres.index(promedio_min)
indice_max = nombres.index(promedio_max)

print(f"Promedio mas bajo: {promedio_min} ({nombres[indice_min]})")
print(f"Promedio mas alto: {promedio_max} ({nombres[indice_max]})")

calificaciones_ordenadas= sorted(promedio_alumno)
print (f"las calificaciones ordenadas son {calificaciones_ordenadas}")


buscar = int(input("Ingresa la calificación que quieres buscar: "))

# Revisamos en qué alumnos aparece esa calificación
encontrados = []
for i in range(b):
    if buscar in calificaciones[i]:
        encontrados.append(nombres[i])

if encontrados:
    print(f"La calificación {buscar} la tienen: {', '.join(encontrados)}")
else:
    print(f"Ningún alumno tiene la calificación {buscar} ")

