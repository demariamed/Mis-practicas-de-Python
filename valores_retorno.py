
# # Valores de retorno sentencia return

# # # def promedio (*numeros):
# #     return sum(numeros)/len(numeros) # La sentencia 'return' termina la ejecucion de la funcion de una forma similar a la sentencia break, conserva el valor de la operacion que estaba despues de esta sentencia para llevarsela al ambito superior

# # x = promedio(4,5,6)
# # print(x)

# def area(**dato): # ** dato es una variable que recibe un diccionario
#     ''' Calcula el area de una figura geometrica y la imprime en pantalla. ''' # Docstring

#     # Si el diccionario tiene una clave llamada 'figura' evalua el valor de la clave 
#     if dato["figura"]=="Rectangulo":
#         return (dato["base"]*dato["altura"]) #Si el valor de la clave es 'Rectangulo' imprime el valor de la clave 'base' multiplicado por 'altura'
#     elif dato["figura"]=="Triangulo":
#         return (dato["base"]*dato["altura"]/2) #Si el valor de la clave es 'Triangulo' imprime el valor de la clave 'base' multiplicado por 'altura' divido entre 2
#     elif dato["figura"]=="Circulo":
#         return int(3.141593*dato["radio"]**2) #Si el valor de la clave es 'Circulo' imprime el valor de la clave 'radio' al cuadrado por 'Pi'
#     else:
#         print("Figura desconocida") #Si el valor de la clave no es ninguna de las anteriores, imprime "Figura desconocida"

# # Ejemplo de llamada a la funcion 

# triangulo = area(figura = 'Triangulo', base = 10, altura = 5) # Llama a la funcion area con los parametros 'figura', 'base', y 'altura'
# print (f'El area del triangulo es: {triangulo}')
# circulo = area(figura = 'Circulo', radio = 10, color = 'Rojo') # Llama a la funcion area con los parametros 'figura', 'radio', y 'color'
# print (f'El area del circulo es: {circulo}')
# dodecagono = area(figura = 'Dodecagono', lado = 10) # Llama a la funcion area con los parametros 'figura' y 'lado'
# print (f'El area del dodecagono es: {dodecagono}')

# ##########################################################################################################

# # Recursividad de funciones en Python
#  # El factorial de un numero corresponde a la cantidad de multiplicar un numero por todos los numeros naturales anteriores
#  # Por seguridad Python indica que el limite de recursividad nativa es de 1000

# def factorial(numero):
#     if numero == 0:
#         return 1
#     else:
#         return numero * factorial(numero - 1)

# print('El factorial de 0 es (0!):' ,factorial (0))
# print('El factorial de 1 es (1!):' ,factorial (1))
# print('El factorial de 3 es (3!):' ,factorial (3))

# # Caso: RecursionError: maximum recursion depth exceeded while calling a Python object

# def factorial(numero, intentos = 0):
#     if numero == 0:
#         return 1
#     else:
#         intentos += 1
#         print(intentos)
#         return numero * factorial(numero - 1, intentos)

# print('El factorial de -1 es (-1!):' ,factorial (-1))

###############################################################################33

# Funciones lamda o funciones anonimas


# # Definiendo una funcion lambda y los parametros dentro de ella, sin nombre de la funcion, en bloque y de manera sencilla

# suma = lambda x,y : x + y 
# print(suma('Hola','Mundo'))
# print(suma(2,5))


# # Lista de numeros ordenada  

# lista_numeros = [1,0,-2]
# lista_numeros = sorted(lista_numeros)
# print(lista_numeros)

# #Lista de numeros ordenada segun su valor absoluto que es equivalente al mismo numero pero en positivo, agregamos un nuevo parametro.

# lista_numeros = [1,0,-2]
# lista_numeros = sorted(lista_numeros, key = lambda n: abs(n))
# print(lista_numeros)

############################################################

# Funcion zip usualmente en compañia de un ciclo for
# zip sirve para realizar emparejamientos entre listas, tuplas o elementos iterables
# Toma  la iterable con la menor cantidad de elementos

paises = ['Kenia', 'Francia', 'Mexico', 'Japon']
capitales = ['Nairobi', 'Paris', 'Ciudad de Mexico', 'Tokio']
poblacion = [54, 66, 130]

for i in zip(paises, capitales, poblacion):
    print(i)