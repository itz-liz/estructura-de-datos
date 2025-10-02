# Itzel Cortes Aguirre - Ejercicio 4
# Diseñe un algoritmo recursivo que permita calcular la suma de todos los elementos de enteros con esto realizar un arreglo
# El arreglo lo debe de recorrer sin utilizar ciclos y la dimension del mismo es parte del dato de entrada
# Al inicio se pregunta el tamaño del arreglo y dimension, con esto se pide despues los numero dentro del arreglo
# despues de ello tiene que salir la suma de numeros enteros
while True:

    def llenar_y_sumar_matriz(h, a):
    #llena la matriz con los datos dados
        if h <= 0 or a <= 0:
            print("Dimensiones inválidas. La altura y el ancho deben ser mayores que cero.")
            return

        matriz = []
        print("\n Ingresa los datos para la matriz")
        for i in range(h):
            fila = []
            for j in range(a):
                try:
                    valor = int(input(f"Ingresa el número en la posición [{i}][{j}]: "))
                    fila.append(valor)
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número.")
                    return
            matriz.append(fila)

        print("\n Tu arreglo ingresado es:")
        for fila in matriz:
            print(*fila)
    
        print("\n Suma por fila")
        for i, fila in enumerate(matriz):
            print(f"Suma de la fila {i}: {sum(fila)}")


    try:
        altura = int(input("Ingresa la altura de tu arreglo: "))
        ancho = int(input("Ingresa el ancho de tu arreglo: "))
        llenar_y_sumar_matriz(altura, ancho)
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número para las dimensiones.")

    h = int(input("Ingresa la altura de tu arreglo: "))
    a = int(input("Ingresa el ancho de tu arreglo: "))

