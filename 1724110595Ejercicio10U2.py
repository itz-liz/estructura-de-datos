# En una sucursal bancaria se atienden a los clientes, pero existen dos 
# tipos de clientes normales y preferentes (personas mayores, embarazadas, 
# con algún tipo de discapacidad, entre otras).

# El sistema debe gestionar dos colas independientes: 
# 1- una para clientes preferentes 
# 2- otra para clientes normales

# El orden de atención es el siguiente: 
# 1- siempre que haya clientes preferentes se atienden primero 
# 2- si no hay clientes preferentes, se atiende a los clientes normales

# El programa debe permitir:
# 1- agregar un cliente a la cola correspondiente 
# 2- atender al siguiente cliente según las reglas 
# 3- mostrar el estado de ambas colas
# 4- salir del sistema

cola_preferente = []
cola_normal = []

while True:
    print("____Banco____")
    print("A) Agregar cliente")
    print("B) Atender cliente")
    print("C) Mostrar colas")
    print("D) Salir")

    opcion = input("Elige una opción: ").lower()

    if opcion == "d":
        print("Adios empleado con sueldo minimo. Haz salido,Gracias.")
        break

    elif opcion == "a":
        nombre = input("Nombre del cliente: ")

        print("Tipo de cliente:")
        print("1) Preferente")
        print("2) Normal")
        tipo = input("Elige entre 1 o 2: ")

        if tipo == "1":
            cola_preferente.append(nombre)
            print(f"Cliente preferente '{nombre}' agregado.")
        else:
            cola_normal.append(nombre)
            print(f"Cliente normal '{nombre}' agregado.")

    elif opcion == "b":
        if cola_preferente:
            atendido = cola_preferente.pop(0)  
            print(f"Atendiendo a cliente preferente: {atendido}")
        elif cola_normal:
            atendido = cola_normal.pop(0) 
            print(f"Atendiendo a cliente normal: {atendido}")
        else:
            print("No hay clientes para atender.")

    elif opcion == "c":
        print("\nCola preferente:")
        for cliente in cola_preferente:
            print("-", cliente)

        print("Cola normal:")
        for cliente in cola_normal:
            print("-", cliente)

    else:
        print("Opción inválida, intenta de nuevo.")

