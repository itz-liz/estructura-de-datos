#En una fabrica los productos terminados deben pasar por un proceso de inspección de calidad antes de ser empacados. 
#Debido a alta demanda, los productos llegan continuamente a la estación de inspección y se van acumulando en una cola 
#de espera además cuando un producto no pasa la inspección debe ser enviado a una cola de retrabajo donde será preparado. 
#El flujo funciona de la siguiente manera:
#1. los productos llegan a el área de calidad (cola de inspección)
#2. el inspector toma el producto (FIFO), lo revisa y decide:
#   a) aprobado (se registra en la lista de productos finalizados) 
#   b) rechazado (pasa a la cola de retrabajo)
#3. los productos en retrabajo pueden ser procesados después considerando también "FIFO" 
#el programa debe permitir registrar los productos de entrada 
#reconocer cuales son los productos aceptados y no aceptados
#revisar la fila de retrabajo y registrar que productos de retrabajo han sido aceptados

# Colas
inspeccion = []     
retrabajo = []      
finalizados = []    

while True:
    print("___Control de calidad de Productos___")
    print("A) Registrar producto a inspección")
    print("B) Revisar siguiente producto")
    print("C) Mostrar retrabajo")
    print("D) Procesar producto de retrabajo")
    print("E) Mostrar productos finalizados")
    print("F) Salir")
    eleccion = input("Elige: ").upper()

    if eleccion == "A":
        prod = input("Nombre del producto: ")
        inspeccion.append(prod)
        print(f"'{prod}' agregado a inspección")

    elif eleccion == "B":
        if not inspeccion:
            print("No hay productos en o para inspección")
        else:
            prod = inspeccion.pop(0)
            print(f"__Revisando '{prod}'__")
            res = input("¿Aprobado? (s/n): ").lower()
            if res == "s":
                finalizados.append(prod)
                print(f"'{prod}' aprobado")
            else:
                retrabajo.append(prod)
                print(f"'{prod}' enviado a retrabajo")

    elif eleccion == "C":
        if not retrabajo:
            print("No hay productos en retrabajo")
        else:
            print("__Retrabajo:__")
            for p in retrabajo:
                print("-", p)

    elif eleccion == "D":
        if not retrabajo:
            print("No hay productos en retrabajo")
        else:
            prod = retrabajo.pop(0)
            print(f"__Procesando retrabajo '{prod}'__")
            r = input("¿Aprobado ahora? (s/n): ").lower()
            if r == "s":
                finalizados.append(prod)
                print(f"'{prod}' ahora está aprobado")
            else:
                retrabajo.append(prod)
                print(f"'{prod}' volvió a retrabajo")

    elif eleccion == "E":
        if not finalizados:
            print("Aún no hay productos finalizados")
        else:
            print("__Finalizados:__")
            for p in finalizados:
                print("-", p)

    elif eleccion == "F":
        print("Acabas de salir de el menu")
        break

    else:
        print("Opción no válida.Intenta de nuevo")

