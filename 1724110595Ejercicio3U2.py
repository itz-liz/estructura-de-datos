#Verificar utilizando pilas si una palabra es un palindromo o no lo es:
#1. Solicitar al usuario la palabra
#2. Utilizar la pila para invertir la palabra
#3. Comparar
#invertida (si son iguales = palindromo y si son diferentes debe decir que no es palindromo)
pila = []

while True:
    print("para salir escribe [bye]")
    palabra = input("Escribe una palabra: ")

    if palabra.lower() == "bye":
        print("Programa acabado:3")
        break

    for letras in palabra:
        pila.append(letras) 

    palindromo = ""
    while pila:
        palindromo += pila.pop()

    if palabra == palindromo:
        print(f"La palabra si es un palindromo porque {palabra} alreves es igual que {palindromo}")
    else:
       print(f"La palabra no es un palindromo porque {palabra} alreves no es igual que {palindromo}")

