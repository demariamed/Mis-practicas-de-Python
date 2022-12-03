vocales = ('a','e','i','o','u')

print(vocales[2])

# vocales[2] ='I' error, no podemos modificar valores definidos, en este caso de mayusculas a minusculas

print(vocales[:3] + vocales[2:]) #concatenacion sin mofidicacion

print(vocales)

print(vocales.index('o')) #imprimir el indice de un valor

lista_vocales = list(vocales) #esta funcion nos devuelve una lista a partir de una tupla

lista_vocales[2]= 'I'

print(lista_vocales) #modificar el valor de esta tupla

tupla_vocales = tuple(lista_vocales) #convertir de una lista a una tupla

# tupla_vocales[2] = 'I' error porque en una tupla no podemos modificar sus valores
