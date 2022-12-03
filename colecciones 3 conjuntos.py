# canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'platano'}

# print(canasta)

# print('manzana' in canasta)

# print('melon' in canasta)

# vocales =['a','e','i','o','u','a']

# print(vocales)

# vocales = list(set(vocales)) #para convertir en conjunto y luego a lista el valor que sea arrojado

# print(vocales)

# vocales ={'a','e','i','o','u','a'} #conjunto con valores repetidos
 
# vocales2 ={'e','i','o'} #creando un nuevo conjunto

# print(vocales2.issubset(vocales)) #indica si un conjunto es un subconjunto dentro de otro

# vocales2 ={'e','i','y'} #probando con un nuevo conjunto 

# print(vocales2.issubset(vocales)) #arrojara false porque un valor del conjunto no coincide

vocales1 = {'a','e','i','o','u'}

vocales2 = {'A','E','I','O','u'}

print(vocales1 - vocales2) #imprimir la diferencia de ambos conjuntos

print(vocales1 | vocales2) #imprimir la union de ambos conjuntos

print(vocales1 & vocales2) #imprimir la interseccion de elementos que estan en ambos conjuntos

print(vocales1 ^ vocales2) #diferencia simetrica, valores que estan en cualquiera de los conjuntos
