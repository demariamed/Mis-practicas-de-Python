# # Programa que simula el comportamiento de un dado

# import random # Definiendo funcion ramdom

# print("El dado dio: " + str(random.randint(1,20))) # Asignando limites, el limite inferior del rango y luego su limite superior

#############################################################################3

# Programa que tira un dado 'n' cantidad de veces

import random

def tiro_dado(num_tiros) : # Asignando un parametro 'num_tiros'
    for dado in range(num_tiros) : # Estableciendo rango con ciclo for
        print("El dado  " + str(dado + 1) + " dio: " + str(random.randint(1,6))) # Impresion del dado, conversion str y agregar al 1 para empezar a contar desde le cero y concatenar con 'dio' asi como con str(random.randint(1,6))

tiro_dado(5) # Numero de veces que se tirara el dado
