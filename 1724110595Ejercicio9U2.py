# En una oficina ahy una impresora compartida, los empleados envian sus documentos para imprimir y los trabajos se van formando
# en una cola de impresion.
# El programa debe permitir: 
# 1) enviar un nuevo documento a la cola
# 2) imprimir (eliminar) el primer documento en la cola
# 3) mostrar los documentos en espera
# 4) salir del programa
# Condicion: en una cola de impresion para una oficina y por la carga en la misma se debe poder etiquetar un mandato de imppresion 
# con tres categorias: urgente, normal, postergado. Las anteriores condiciones deberan ser tomadas en la cola y formar las peticiones
# de impresion considerando las etiquetas 

cola = []

while True: 
    print ("Menu de seleccion:")
    print("A) Enviar documento a la cola")
    print("B) Imprimir cola y Eliminar el primer documento de la cola")
    print("C) Mostrar documentos de Espera")
    print("D) Salir")
    operacion = str(input("Ingresa la letra de la operacion a realizar:"))
    
    if operacion.lower() == "d":
        print("Documentos acabados, adios")
        break
