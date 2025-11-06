# Cree un programa que permita al usuario ingresar una linea de texto y que cuente cuantas letras dependiendo la eleccion
# existen en esa linea de texto, el usuario podra elegir cualquier letra del alfabeto ya sea mayuscula o minuscula y el 
# sistema entregara el numero de veces que esa letra aparece esa letra repetida, utilice una pila para el desarrollo

while True:
    print("para salir escribe [adios]")
    linea =(input("Escribe lo que tu quieras:"))
    letra =(input("Ingresa la letra a buscar:"))

    
    pila =[]

    for i, caracter in enumerate(linea):
        if caracter == letra:          
            pila.append((i, caracter)) 
            print(f"Coincidencia en el puesto {i}: '{caracter}'")

    print(f"La letra '{letra}' aparece {len(pila)} veces en la línea.")