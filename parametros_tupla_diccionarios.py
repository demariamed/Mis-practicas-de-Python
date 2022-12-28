# # Parametros de tipo Tupla o *args
# # Accciones para un cantidad indeterminada de elementos

# def promedio (*numeros):
#     '''
#     Recibe un solo parametro de tipo tupla, de valores numericos
#     E imprime su promedio
#     '''
#     promedio = sum(numeros)/len(numeros)
#     print('El promedio es:', promedio)

# promedio(4)
# promedio(4, 5, 6)
# promedio(1, 2, 3, 4, 5, 6, 7, 8, 9,)


# def es_numero(titulo,*serie):
#     '''
#     Imprime un titulo
#     Verifica si el caracter en el parametro de tipo tupla es un numero o no
#     '''
#     print(titulo)
#     for i in serie:
#         if type(i) == int or i.isdigit(): #para ver si es un elemento de tipo entero o digito
#             print(f'{i} es numero')
#         else:
#             print(f'{i} no es numero')

# # Llamando a nuestra primera funcion con una serie de numeros y letras
# es_numero('Numeros', '1','2','3')
# es_numero('Letras','a','b','c')

# # Invocando por medio de variables
# nombre = 'Mezcla' # Cadena 
# lista_varios = ['a', '2', 3, 'f', 5] # definiendo lista 
# es_numero(nombre, *lista_varios) # definiendo variable e indicandole a Python con * que va a recibir multiples valores en el parametro

#######################################################################

# Parametros de tipo diccionario o **kwargs

def area(**dato): # ** dato es una variable que recibe un diccionario
    ''' Calcula el area de una figura geometrica y la imprime en pantalla. ''' # Docstring

    # Si el diccionario tiene una clave llamada 'figura' evalua el valor de la clave 
    if dato["figura"]=="Rectangulo":
        print(dato["base"]*dato["altura"]) #Si el valor de la clave es 'Rectangulo' imprime el valor de la clave 'base' multiplicado por 'altura'
    elif dato["figura"]=="Triangulo":
        print(dato["base"]*dato["altura"]/2) #Si el valor de la clave es 'Triangulo' imprime el valor de la clave 'base' multiplicado por 'altura' divido entre 2
    elif dato["figura"]=="Circulo":
        print(3.141593*dato["radio"]**2) #Si el valor de la clave es 'Circulo' imprime el valor de la clave 'radio' al cuadrado por 'Pi'
    else:
        print("Figura desconocida") #Si el valor de la clave no es ninguna de las anteriores, imprime "Figura desconocida"

# Ejemplo de llamada a la funcion 

area(figura = 'Triangulo', base = 10, altura = 5) # Llama a la funcion area con los parametros 'figura', 'base', y 'altura'
area(figura = 'Circulo', radio = 10, color = 'Rojo') # Llama a la funcion area con los parametros 'figura', 'radio', y 'color'
area(figura = 'Dodecagono', lado = 10) # Llama a la funcion area con los parametros 'figura' y 'lado'
