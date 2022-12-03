# vocales = ['a', 'e', 'i', 'o', 'u']

# vocales[1:4] = ['E', 'I', 'O']

# print(vocales, len(vocales)) #tamaño de la lista

# vocales[1:4] = [] #eliminar valores de la lista

# print (vocales, len(vocales))

# vocales[1:2] = ['e', 'i', 'o', 'u']

# print (vocales, len(vocales)) #cambiar posicion segun un indice

# vocales.extend(['i','i']) #fusionar listas

# print(vocales.index('i')) #busca un valor y devuelve su índice

# print(vocales.count('i')) #busca valores repetidos

# print(vocales.index('i', 4)) #posicion o lugar

# vocales.reverse() #revertir el orden 

# print(vocales, len(vocales))

# vocales.sort() #ordenar listas

# print(vocales, len(vocales))

# carros = ['Audi', 'Ford', 'BMW', 'VW']

# carros.sort(key=len) #metodo sort + key para identificar la longitud de elementos

# print(carros)

# listas = [[0], [2,3,4], [5,6]]

# print(listas[0], listas[1:3]) #Imprimir por separado

# print(listas[2][1]) #Impirmir un solo valor de una lista dentro de una lista

vocales1 = ['a', 'e', 'i', 'o', 'u']

vocales2 = vocales1

print(vocales1, vocales2) #igualar valores

print(id(vocales1), id(vocales2)) #duplicar el mismo objeto para optimizar el espacio de memoria

vocales3 = vocales1.copy () #asignar diferentes identificadores

print(vocales1,vocales3) #Se observan valores iguales 

print(id(vocales1), id(vocales3)) #Se observan diferentes identificadores

print(id(vocales1[2])) #imprimir id de un solo valor de la lista

print(id(vocales1[2]), id(vocales2[2])) #imprimir valor del mismo objeto

print(id(vocales1[2]), id(vocales3[2])) #imprimir id de otro objeto

del vocales1[2] #eliminar un valor

print(vocales2,vocales3) 

print(id(vocales1[2]), id(vocales3[3]))







