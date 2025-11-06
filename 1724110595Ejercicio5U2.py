# desarrollar un programa que evalúe una línea de texto 
#  y cuente, el número de caracteres especiales que se escriben en la línea.
# la línea de texto no tiene límite y al finalizar el último valor entregado será el número de caracteres especiales 
# incluyendo el espacio. Utilice una pila para el desarrollo

pila = []

while True: 
    print("para salir escribe [salir]")
    especial = (input("Escribe alguna frase, palabra, texto:"))

    if especial.lower() == "salir":
        print("Programa acabado:3")
        break

    for c in especial:
        pila.append(c)  

    contador = 0

    while pila:
        simbolo = pila.pop()  
        if not simbolo.isalnum() and simbolo != " ":  
            contador += 1

    print("La cantidad de caracteres especiales es:", contador)
