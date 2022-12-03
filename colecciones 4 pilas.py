pila = [3,6,7]

while len(pila) >= 3: #para revisar el ciclo
    if pila[-1] % 3: #verificar si el ultimo elemento de la pila es divisible entre 3

        extraido = pila.pop() #para extraer el ultimo elemtno de la pila
        pila.append(extraido + 1)
        print(pila)
        
    else : 
        print("Todos los elementos de la pila son multiplos de 3")
        break 


