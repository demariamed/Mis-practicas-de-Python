### <<m_alumnos.py>>

"""

Este modulo contiene la funcion captura que solicita la informacion de los 
alumnos y la funcion promedio que calcula el promedio de cada alumno

"""

# Retoma el ejercio de la semana pasaba y las funciones definidas en el
# Las almacenaras en un nuevo archivo llamado m-alumnos.py
# Reescribiras el programa principal para resolverlo haciendo un import a tu modulo y asignandole un alias
# Hacer un script que contenga las funciones a utilizar


def captura_alumnos(numero = 3):
    '''
    Registra alumnos y dos calificaciones
    Recibe como parametro la cantidad de alumnos a registrar
    Si no se especifica el numero de alumno, se registraran 3
    '''
    lista_alumnos = []
    for i in range (numero):
        nombre = input(f'{i + 1}.- Ingrese el nombre del alumno: ').capitalize()
        calificacion1 = int(input(f'Ingrese la primera calificacion de {nombre}: '))
        calificacion2 = int(input(f'Ingrese la segunda calificacion de {nombre}: '))
        lista_alumnos.append([nombre, calificacion1, calificacion2])
        promedio(nombre, calificacion1, calificacion2)
    print('Las calificaciones de los alumnos son:', lista_alumnos)

def promedio(nombre, calificacion1, calificacion2):
    '''
    Calcula el promedio de un alumno y lo despliega en pantalla por medio de un mensaje
    Recibe como parametros el nombre y dos calificaciones del alumno
    ''' 
    promedio = (calificacion1 + calificacion2) / 2
    print(f'El promedio de {nombre} es: {promedio}')
    



# numero_alumnos = input('¿Cuantos alumnos se desea registrar?: ')

# if numero_alumnos.isdigit(): #Para saber si es un digito
#     numero_alumnos = int(numero_alumnos)
#     captura_alumnos(numero_alumnos)
# else:
#     captura_alumnos()
