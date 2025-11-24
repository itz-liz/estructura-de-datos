# Una cafeteria recibe pedidos de los clientes en orden de llegada. Cada pedido se agrega a la cola de pedidos pendiente s
# El programa debe permitir:
# A) Registrar un nuevo pedido (Nombre del cliente y tipo de bebida)
# B) Atender el siguiente pedido (El que llego primero)
# C) Consultar los pedidos pendientes 
# D) Consultar los pedidos completados 
# E) Salir del sistema 
# La atencion se realiza por orden de llegada, sin embargo todos aquellos clientes que soliciten el cafe del dia (Americano)
# se corren en la fila y se les atiende antes que cualquier otro producto con mayor elaboracion.
# Cree tambien un catalogo de 5 productos y asigne n nivel de prioridad tipo "El cafe del dia"
# Considerando el tiempo de elebaoracion

catalogo = ["Americano", "Té frío", "Capuchino", "Matte", "Malteada"]

pendientes = []   
completados = []

while True:
    print("\n--- Cafetería: Una Mañana---")
    print("A) Registrar pedido")
    print("B) Atender pedido")
    print("C) Ver pendientes")
    print("D) Ver completados")
    print("E) Salir")
    opcion  = input("Elige: ").upper()

    if opcion == "A":
        nombre = input("Nombre del cliente: ")
        print("____Catalogo de Bebidas____")
        for i, bebida in enumerate(catalogo, 1):
            print(f"{i}) {bebida}")
        eleccion = int(input("Escoge una bebida por su numero:"))

        if 1 <= eleccion <= len(catalogo):
            bebida = catalogo[eleccion - 1]
            pendientes.append((bebida, nombre))
            print(f"Pedido agregado de: {nombre} con: {bebida}")
        else:
            print("No existe esa bebida")

    elif opcion == "B":
        if not pendientes:
            print("No hay pedidos.")
        else:

            prioridad = None
            for i, pedido in enumerate(pendientes):
                if pedido[0] == "Americano":
                    prioridad = i
                    break

            if prioridad is None:
                prioridad = 0
            
            atendido = pendientes.pop(prioridad)
            completados.append(atendido)
            print(f"Preparando el pedido de: {atendido[1]} con la bebida: {atendido[0]}")

    elif opcion == "C":
        if not pendientes:
            print("Sin pendientes.")
        else:
            print("\n Pendientes:")
            for b, n in pendientes:
                print(f"{n} con {b}")

    elif opcion == "D":
        if not completados:
            print("Nada completado.")
        else:
            print("Pedidos Completados:")
            for b, n in completados:
                print(f"{n} que pidio {b}")

    elif opcion == "E":
        print("Gracias por comprar, nos vemos despues!")
        break

    else:
        print("Opción inválida, intenta de nuevo.")
