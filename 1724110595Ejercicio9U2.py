# En una oficina y una impresora compartida, los empleados envian sus documentos para imprimir y los trabajos se van formando
# en una cola de impresion.

# El programa debe permitir: 
# 1) enviar un nuevo documento a la cola
# 2) imprimir (eliminar) el primer documento en la cola
# 3) mostrar los documentos en espera
# 4) salir del programa

# Condicion: en una cola de impresion para una oficina y por la carga en la misma se debe poder etiquetar un mandato de imppresion 
# con tres categorias: urgente, normal, postergado. Las anteriores condiciones deberan ser tomadas en la cola y formar las 
# peticiones de impresion considerando las etiquetas 

cola = []

while True: 
    print ("Menu de seleccion:")
    print("A) Enviar documento a la cola")
    print("B) Imprimir cola y Eliminar el primer documento de la cola")
    print("C) Mostrar documentos de Espera")
    print("D) Salir")
    operacion = str(input("Ingresa la letra de la operacion a realizar:")).strip().lower()

    if operacion == "d":
        print("Documentos acabados, adiós humano :3")
        break

    elif operacion == "a":
        nombre = input("Nombre del documento: ").strip()

        print("Categorías disponibles:")
        print("1) Urgente")
        print("2) Normal")
        print("3) Postergado")
        opcion = input("Elige la categoría (1/2/3): ").strip().lower()

        if opcion == "1":
            categoria = "Urgente"
        elif opcion == "2":
            categoria = "Normal"
        elif opcion == "3":
            categoria = "Postergado"
        else:
            print("Categoría inválida, se asignará como 'Normal'")
            categoria = "Normal"

        cola.append((categoria, nombre))
        print(f"Documento '{nombre}' agregado como {categoria}")

    elif operacion == "b":
        if not cola:
            print("No hay documentos para imprimir.")
        else:
            prioridades = ["Urgente", "Normal", "Postergado"]
            impreso = False
            for nivel in prioridades:
                for i, doc in enumerate(cola):
                    if doc[0] == nivel:
                        imprimir = cola.pop(i)  # .pop() aquí
                        print(f"📄 Imprimiendo documento: '{imprimir[1]}' [{imprimir[0]}]")
                        impreso = True
                        break
                if impreso:
                    break

            if not impreso:
                imprimir = cola.pop(0)
                print(f"Imprimiendo documento: '{imprimir[1]}' [{imprimir[0]}]")

    elif operacion == "c":
        if not cola:
            print("No hay documentos en espera.")
        else:
            print("\n📌 Documentos en cola:")
            for idx, doc in enumerate(cola, start=1):
                print(f"{idx}. {doc[1]} [{doc[0]}]")

    else:
        print("Opción no válida, intenta de nuevo...")
    
 