# Simule un sistema de atención en una cafetería donde los clientes llegan, se forman en una cola
# y hacen sus pedidos. El programa debe permitir:
# 1) Agregar un cliente a la cola con su pedido
# 2) Atender (servir) al primer cliente de la cola
# 3) Mostrar la cola actual de clientes
# 4) Mostrar aquellos clientes que pidieron el café del día (Americano)
# 5) Salir del programa
# Los clientes se agregan al final de la cola y se atienden en el orden en que llegaron (FIFO).
# El café del día es Americano y debe ser identificado especialmente.

cola = []

while True:
    print("\n=== Cafetería - Sistema de Cola ===")
    print("A) Agregar cliente a la cola")
    print("B) Atender al primer cliente")
    print("C) Mostrar cola actual")
    print("D) Mostrar clientes que pidieron café del día (Americano)")
    print("E) Salir")
    operacion = str(input("Ingresa la letra de la operación a realizar: "))
    
    if operacion.lower() == "e":
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        break
    
    elif operacion.lower() == "a":
        nombre = input("Ingresa el nombre del cliente: ")
        print("\nMenú de Café:")
        print("1. Americano (Café del día)")
        print("2. Capuchino")
        print("3. Latte")
        print("4. Espresso")
        pedido = input("Ingresa el pedido del cliente: ")
        
        # Agregamos al cliente con su pedido a la cola
        cola.append({"nombre": nombre, "pedido": pedido})
        print(f"\n{nombre} se agregó a la cola con pedido: {pedido}")
    
    elif operacion.lower() == "b":
        if cola:
            cliente_atendido = cola.pop(0)
            print(f"\nAtendiendo a {cliente_atendido['nombre']}")
            print(f"Pedido: {cliente_atendido['pedido']}")
            print(f"{cliente_atendido['nombre']} ha sido atendido y salió de la cola")
        else:
            print("\nNo hay clientes en la cola")
    
    elif operacion.lower() == "c":
        if cola:
            print("\n=== Cola Actual ===")
            for i, cliente in enumerate(cola, 1):
                print(f"{i}. {cliente['nombre']} - Pedido: {cliente['pedido']}")
        else:
            print("\nLa cola está vacía")
    
    elif operacion.lower() == "d":
        # Mostrar clientes que pidieron café del día (Americano)
        clientes_cafe_dia = [c for c in cola if "americano" in c['pedido'].lower()]
        if clientes_cafe_dia:
            print("\n=== Clientes que pidieron Café del Día (Americano) ===")
            for i, cliente in enumerate(clientes_cafe_dia, 1):
                print(f"{i}. {cliente['nombre']} - {cliente['pedido']}")
        else:
            print("\nNo hay clientes que hayan pedido el café del día")
    
    else:
        print("\nOpción no válida. Por favor ingresa una opción del menú")
