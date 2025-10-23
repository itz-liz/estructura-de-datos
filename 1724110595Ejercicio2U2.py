#Cree un programa en Python que determine, si una expresión tiene los paréntesis correctamente balanceados para ello utilice una 
# pila que almacene los paréntesis de apertura y lo retire cuando encuentre un paréntesis de cierre 
# Una expresión está balanceada si: 
# cada paréntesis de apertura tiene su correspondiente cierre. No hay cierres antes de que haya un paréntesis de apertura
#pila.pop

while True:
    print("Si quieres salir escribe *adios* ")
    expresion = (input("ingresa la expresion a balancear: "))
    
    if expresion.lower() == "adios":
        print("bye bye :P")
        break

    pila = []  # pila para cada expresion
    balanceada = True #mientras sea verdadera la suposicion

    for simbolo in expresion:
        if simbolo == "(":
            pila.append(simbolo)  
        elif simbolo == ")":
            if pila:  
                pila.pop()  
            else:
                # Aqui buscamos si para cada : ( tiene un : )
                balanceada = False
                break

    if balanceada and not pila:
        print("Tu expresion esta balanceada")
    else:
        print("Tu expresion no esta balanceada")
    