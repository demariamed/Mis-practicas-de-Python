# def sumar(parametro1, parametro2):
#     '''Funcion que suma dos parametros y los imprime en pantalla'''
#     print('Suma:', parametro1 + parametro2)

# argumento1 = 5
# argumento2 = 7

# # Invocando a la funcion por medio de parametros variables
# sumar(argumento1, argumento2)

# # Invocando a la funcion por medio de parametros de valor 

# sumar('mundo!', 'Hola ')
# sumar('Hola', 'mundo! ')

# sumar('hola')

##########################################################################################################

# Parametros opcionales

def muestra_alumno(nombre, edad = 18, sexo = 'F'):
    '''
    Es una funcion que muestra en pantalla el nombre, la edad y el sexo de un alumno
    Recibe tres parametros.
    1.- Nombre
    2.- Edad = 18
    3.- Sexo = 'F'
    '''
    print(f'nombre:{nombre}, Edad: {edad}, Sexo: {sexo}')

# Ejecucion de funcion con parametro obligatorio
muestra_alumno(' Maria')

#Ejecucion utilizando el parametro obligatorio y uno opcional
muestra_alumno(' Maria', 22)

#Ejecucion de funcion con el primer y ultimo parametro
muestra_alumno(' Juan', sexo ='M')

