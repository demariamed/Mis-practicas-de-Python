# Que solicite al usuario cierto numero de personas para agregar a un formulario
# Que, primero, solicite el nombre de todas las personas que se ingresaran
# Que, despues, pregunte la edad de cada persona
# Que, luego, pregunte el sexo de cada persona, feririendose a ella por su nombre
# Si no se especifica el sexo, su guarda la variable como 'No especificado'
# Se unen los tres datos introducidos en una tupla por persona y se imprime en la pantalla
# Usar al menos una funcion


def agregar_datos(lista, valor):
    '''
    Funcion que agrega un dato a una lista especificada
    '''
    if valor == '':
        valor = 'No especificado'
    lista.append(valor)
    return lista

nombres = []
edades = []
sexos = []

personas = int(input('¿Cuantas personas se quiere registrar?: '))

for i in range(personas):
    nombre = input(f'Ingrese el nombre de la persona {i+1}: ').title()
    nombres = agregar_datos(nombres, nombre)
for i in range(personas):
    edad = input(f'Ingrese la edad de {nombres[i]}: ')
    edades = agregar_datos(edades, edad)
for i in range(personas):
    sexo = input(f'¿Cual es el sexo de {nombres[i]}?: ')
    sexos = agregar_datos(sexos,sexo)
for i in zip(nombres, edades, sexos):
    print(i)
