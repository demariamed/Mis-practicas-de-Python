# Bucle infinito que que solicita al usuario una letra
# Especificar al usuario la condicion para terminar el programa
# Funcion que imprima en la pantalla la letra siguiente en el alfabeto y la letra anterior a la ingresada
# El usuario continuara en el bucle hasta que el usuario decida salir del programa
# Distinguie entre mayusculas y minusculas


# abecedario = ["a","b","c","e","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]
# print('Las letras seleccionadas son:', abecedario)
# abecedario = [abecedario.capitalize() for abecedario in abecedario]

def lista_letras (extension = 100):
    '''
    Solicita al usuario una letra de la a a la T
    Imprime en la pantalla la letra anterior y la posterior a la ingresada por orden en el abecedario
    '''
    abecedario = ["a","b","c","e","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]
    for letra in range (extension):
        letra = input(f' Ingrese una letra del abecedario: ').capitalize()
        letra1 = (input(f'Ingrese la letra anterior de {letra}: ')).capitalize()
        letra2 = (input(f'Ingrese la letra posterior de {letra}: ')).capitalize()
        abecedario.append(['Las letras seleccionadas son:', letra1, letra, letra2])
        
    print('Las letras seleccionadas son:', [letra1, letra, letra2])
    

abecedario = input('Bienvenido al ejercicio 9, pulse ENTER para continuar: ')
if abecedario.isdigit():
    abecedario = str(abecedario)
else:
    lista_letras()

# numero_letras = input('Bienvenido al ejercicio 9: ')
# if numero_letras.isdigit(): #Para saber si es un digito
#     numero_letras = str(numero_letras)
#     # lista_letras(numero_letras)
# else:
#     lista_letras()

# def exit ():
#     '''
#     El usuario puede salir del programa escribiendo STOP     
#     '''
# print('Hasta luego')
# exit()    
