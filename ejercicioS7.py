lista = []



alumnos = 0
while alumnos <= 5:
    opcion = input ('Agregar alumno (1) o terminar (2): ')
    if opcion == '1':
        nombre = input('Ingrese el nombre del alumno:').capitalize()
        calificacion1 = int(input(f'Ingrese la primera calificacion de {nombre}: ')) #int para hacerlo de tipo numerico
        calificacion2 = int(input(f'Ingrese la segunda calificacion de {nombre}: '))
        alumno = [nombre, calificacion1, calificacion2]
        lista.append(alumno)
        alumnos += 1
    elif opcion == '2':
        print('El programa ha terminado con {alumnos} alumnos.')
        break
    else:
        print('Se ha ingresado una opcion invalida.')
        continue

print('La lista de alumnos es:')
print(lista)



