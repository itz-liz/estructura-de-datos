# arreglo de 1 * n, que se introduzca un nombre y extraer los dstos inciando por el dato que esta arriba, luego una fila 
nombres = [] #hacemos un arreglo para los nombre 

while True:
    print ("para acabar con la insercion de nombres, escribe *fin* ")
    nombre = str(input("Inserta tu nombre: "))

    if nombre.lower() == "fin": #hacemos un .lower para que no importe si ponen fin o FIN
        print ("hasta la proximaaa :3")
        break

    # Agregamos al arreglo
    nombres.append(nombre)

    print("---Nombres en lista(el primero en entrar es el primero en salir)")
    for nombre in nombres:
        print(nombre) 

    print("---Lista de las letras del nombre")
    pila = nombre [::-1] #los dos puntos es para contar los elementos y el -1 recorre la secuencia de manera inversa
    for n in reversed(pila):  # Mostramos al revés (último primero)
        print(n)

    print ("---Pila de las letras del nombre")
    for i in pila:
        print(i)

    print ("---pila de los nombres acumulados")
    for x in reversed(nombres):  # Mostramos al revés (último primero)
        print(x)