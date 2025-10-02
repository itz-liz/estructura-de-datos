#Diseñe un programa. Declare y cree un arreglo con edades de un grupo de personas
#Calcule e imprima la edad minima y la edad maxima del grupo de personas con el nombre de estas, el promedio de las edades y
#y la mediana del grupo. Permita al usuario agregar una nueva edad al arreglo y mostrar nuevamente los datos actualizados
# Programa: Manejo de edades de un grupo de personas

# Programa: Manejo de edades de un grupo de personas

# Pedir cantidad de personas
n = int(input("¿Cuántas personas deseas registrar? "))

nombres = []
edades = []

# Registrar nombres y edades
for i in range(n):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    nombres.append(nombre)
    edades.append(edad)

# Calcular edad mínima y máxima
edad_min = min(edades)
edad_max = max(edades)
indice_min = edades.index(edad_min)
indice_max = edades.index(edad_max)

# Calcular promedio
suma = 0
for e in edades:
    suma += e
promedio = suma / len(edades)

# Calcular mediana
edades_ordenadas = sorted(edades)
n = len(edades_ordenadas)
if n % 2 == 0:
    i = n // 2
    mediana = (edades_ordenadas[i - 1] + edades_ordenadas[i]) / 2
else:
    mediana = edades_ordenadas[n // 2]

# Mostrar resultados iniciales
print("\n Primeros datos ingresados")
print(f"Edad mínima: {edad_min} ({nombres[indice_min]})")
print(f"Edad máxima: {edad_max} ({nombres[indice_max]})")
print(f"Promedio de edades: {promedio:.2f}")
print(f"Mediana de edades: {mediana}")

# Permitir al usuario agregar nueva persona
nuevo_nombre = input("\nIngresa el nombre de la nueva persona: ")
nueva_edad = int(input("Ingresa la edad de la nueva persona: "))

nombres.append(nuevo_nombre)
edades.append(nueva_edad)

# Recalcular edad mínima y máxima
edad_min = min(edades)
edad_max = max(edades)
indice_min = edades.index(edad_min)
indice_max = edades.index(edad_max)

# Recalcular promedio
suma = 0
for e in edades:
    suma += e
promedio = suma / len(edades)

# Recalcular mediana
edades_ordenadas = sorted(edades)
n = len(edades_ordenadas)
if n % 2 == 0:
    i = n // 2
    mediana = (edades_ordenadas[i - 1] + edades_ordenadas[i]) / 2
else:
    mediana = edades_ordenadas[n // 2]

# Mostrar resultados actualizados
print("\n=== Datos Actualizados ===")
print(f"Edad mínima: {edad_min} ({nombres[indice_min]})")
print(f"Edad máxima: {edad_max} ({nombres[indice_max]})")
print(f"Promedio de edades: {promedio:.2f}")
print(f"Mediana de edades: {mediana}")
