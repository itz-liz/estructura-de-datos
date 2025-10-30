# Cree un programa en python que simule la atención de personas que hacen fila para comprar 
# boletos en una taquilla de cine. Lo clientes llegan, se forman al final de la fila y se van
# atendiendo uno por uno en el orden que llegaron.
#Instrucciones: 
# 1. Cree una cola vacía, puede representarse con una lista
# 2. El programa debe mostrar un menú con las siguientes opciones: A) Llegada del cliente
# B) Vender boletos. c) mOSTRAR fILA actual D) Salir
# 3. Cada vez que llegue un cliente, el programa pedira su nombre, y lo agregara al final de
# la cola
# 4. Al vender un boleto, se debe retirar al final de la cola y mostrar un mensaje 
# (cliente tal, a comprado un boleto)
# 5. Si la cola esta vacia y se intenta atender, el programa mostrará 
# "No hay clientes en la fila"
# 6. La cola actual debe mostrarse en cada interaccion o cuando el usuario lo solicite.
cola=[]

while True: 

    print ("Menu de seleccion:")
    print("A) Llegada de cliente")
    print("B) Vender boletos")
    print("C) Mostrar fila Actual")
    print("D) Salir")
    operacion = str(input("Ingresa la letra de tu operacion:"))
    
    if operacion.lower() == "d":
        print("Acabas de salir, adiooo")
        break

    elif operacion.lower() == "a":
        nombre = input("Inserta el nombre del cliente: ")
        cola.append(nombre)
        print(f"{nombre} se agrego \n")

    elif operacion.lower() == "b":
        if cola: #comparamos la cola 
            cliente = cola.pop(0) #hacemos una variablecon el nombre de cliente que 
            print(f" {cliente} ha comprado un boleto y salió de la fila\n")
        else:
            print("No tenemos clientes\n")  

    elif operacion.lower() == "c":
        cola_copia = cola.copy()  

        print("Tu cola es:")
        while cola_copia:
            print(cola_copia.pop())  

    else:
        print("tu valor no es valido, ingresa algo del menu \n")
    
    
    print("Fila actual:", cola)
    