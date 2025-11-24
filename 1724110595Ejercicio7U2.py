#Desarrolle un programa en Python que simule la atención a clientes en una fila de un banco, 
#los clientes llegan y se agregan al final de la cola y el cajero los atiende en el mismo orden en el que llegaron.
#Hay que crear una cola vacía la cual se puede representar con una lista.
#El programa deberá mostrar un menú con las siguientes opciones:

#A) agregar clientes a la cola
#B) atender al cliente
#C) Mostrar la cola actual 
#D) salir 

#Cada vez que se agregue un cliente, el programa deberá solicitar su nombre.Al atender un cliente, se debe eliminar al primer 
#cliente de la cola y mostrar su nombre con una etiqueta de cliente atendido.
#Si se intenta atender cuando la cola está vacía, el programa debe mostrar un mensaje apropiado. 
#Mostrar la cola actual en cada iteración.
cola = []

while True:
    print("___________________________")
    print("Opciones para Clientes")
    print("A) Agregar cliente a la cola")
    print("B) Atender al cliente")
    print("C) Mostrar la cola actual")
    print("D) Salir")
    print("___________________________")

    opcion = input("Elige una opción: ")

    if opcion.lower() == "a":
        nombre = input("Ingrese el nombre del cliente: ")
        cola.append(nombre)
        print(f"{nombre} ha sido agregado a la cola.")
        print("Cola actual:", cola if cola else "Vacía")

    elif opcion.lower() == "b":
        if cola:
            cliente = cola.pop(0)
            print(f"Se ha atendido a {cliente}")
            print("Cola actual:", cola if cola else "Vacía") 
        else:
            print("No hay clientes por atender")

    elif opcion.lower() == "c":
        print("Cola actual:", cola if cola else "Vacía")

    elif opcion.lower() == "d":
        print("Haz salido de la atención a clientes")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
