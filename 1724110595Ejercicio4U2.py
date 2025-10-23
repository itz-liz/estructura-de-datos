#revertir una cadena de palabras utilizando una pila. Descripcion: cree un programa que permita al usuario ingresar una linea
#  de texto y que utilizando una pila muestre la pila de texto invertida. La linea de texto no tendra maximo de palabras sino 
# que al darle enter mostrara el resultado

while True:
    print("Si quieres salir escribe *bye* ")
    texto = (input(" Ingresa tu palabra a revertir: "))
    
    if texto.lower() == "bye":
        print("adios personita humana")
        break

    pila = [] 

    pila.append(texto)
    
    print("Nombre en pila (primero en entrar ultimo en salir)")
    letras = list(texto) #hacemos una lista con el  texto
    print("Texto invertido: ", end="") #hacemos que gracias a end el texto no baje en lista

    while letras: #mientras la pila tenga letras 
        print(letras.pop(), end="") #el punto pop saca la ultima letra y la devuelve, y el end imprime sin bajatr de la linea
    print() #ponemos estre print comom vacio para salto de linea sin afectar el "end"