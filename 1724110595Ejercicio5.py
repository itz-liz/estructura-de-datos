# Promedio y busqueda de eleemntos en un arreglo 
# diseña un programa en python que:
# 1- Permita declarar y crear un arreglo con calificaciones de un grupo de estudiantes (valores enteros del 0 al 100)
# 2- Calcule el promedio de las calificaciones de cada alumno y de las calificaciones almacenadas en el arreglo 
# 3.- Que permita buscar si una calificacion especifica (ingresada por el usuario) se encuentra en el arreglo 
# 4- Que muestre los resultados de forma clara en la pantalla 
# Programa: Promedio y búsqueda de calificaciones
while True:  # repetimos el ciclo 
    # Pedimos el número de alumnos
    b = int(input("¿Cuántos alumnos tienes? "))
    if b <= 0:
        print("Número inexistente, adiós")
        break

    # Guardamos los nombres en una lista
    nombres = []
    for i in range(b):
        nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
        nombres.append(nombre)

    # Pedimos el número de materias
    m = int(input("¿Cuántas materias tienen los alumnos? "))

    # Creamos un arreglo para calificaciones
    calificaciones = []

    # Recorremos cada alumno y pedimos sus calificaciones
    for i in range(b):
        print(f"\nAlumno: {nombres[i]}")
        notas = []
        for j in range(m):
            cal = int(input(f"  Calificación {j+1}: "))
            # Validamos que la calificación esté entre 0 y 100
            if cal < 0 or cal > 100:
                print("  ⚠️ Calificación no válida, se pondrá 0")
                cal = 0
            notas.append(cal)
        calificaciones.append(notas)

    # Calculamos promedios
    print("\nPromedio por Alumno")
    for i in range(b):
        promedio_alumno = sum(calificaciones[i]) / m
        print(f"{nombres[i]}: {promedio_alumno:.2f}")

    todas = [nota for sublista in calificaciones for nota in sublista]
    promedio_grupo = sum(todas) / len(todas)
    print(f"\nPromedio general del grupo: {promedio_grupo:.2f}")

    buscar = int(input("Ingresa la calificación que quieres buscar: "))

    # Revisamos en qué alumnos aparece esa calificación
    encontrados = []
    for i in range(b):
        if buscar in calificaciones[i]:
            encontrados.append(nombres[i])

    if encontrados:
        print(f"La calificación {buscar} la tienen: {', '.join(encontrados)}")
    else:
        print(f"Ningún alumno tiene la calificación {buscar}")

    repetir = input("\n¿Quieres calcular otro grupo? (s/n): ").lower()
    if repetir != "s":
        print("Adiós :3")
        break
