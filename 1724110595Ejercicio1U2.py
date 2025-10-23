# arreglo de 1 * n, que se introduzca un nombre y extraer los dstos inciando por el dato que esta arriba, luego una fila 
pila = []

while True:
    print("Para acabar con la inserción de nombres, escribe *fin*")
    nombre = input("Inserta tu nombre: ")

    if nombre.lower() == "fin":
        print("Hasta la próximaaa :3")
        break

    # Agregamos (push) el nombre a la pila
    pila.append(nombre)

    print("Pila de nombres")
    for n in pila:
        print(n)

    print("Pila de letras del nombre")
    letras = list(nombre)  # Convertimos el nombre en lista de letras
    for l in letras:
        print(l)

    print("Nombre en pila (primero en entrar ultimo en salir)")
    while letras:  
        print(letras.pop())  # Sacamos y mostramos la última letra

    print("Pila de los nombres:")
    pila_copia = pila.copy()  
    while pila_copia:
        print(pila_copia.pop())  
