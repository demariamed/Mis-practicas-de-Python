# Registro de calificaciones

print ('Registro de Calificaciones.')

calificaciones = [] # EN CONSIDERACIÓN 
promedios = []

total_alumnos = int(input('Ingrese la cantidad de alumnos: '))
alumnos = 0

while alumnos <= total_alumnos :
    print ('¿Qué desea hacer?')
    opcion = input ('Agregar alumno [1] o terminar lista [2]: ')
    if opcion == '1' :
        nombre = input ('Ingrese el nombre del alumno: ').capitalize()
        print ('Debe ingresar al menos una calificación y máximo tres.')
        print ('En caso de haber una sola calificación, registre un cero [0] en las siguientes calificaciones.')
        no_calificaciones = int (input('Ingrese el numero de calificaciones a registrar: '))
        calificacion1 = int(input(f'Calificación 1: '))
        calificacion2 = int(input(f'Calificación 2: '))
        calificacion3 = int (input(f'Calificación 3: '))
        if calificacion1 <= 0 :
            print ('¿Está seguro de la calificación del alumno?')
            confirmacion = input ('Sí [1] o No [2] : ')
            if confirmacion == '1' :
                promedio = ((calificacion1 + calificacion2 + calificacion3) / no_calificaciones)
                promedioT = [nombre, promedio]
                alumno = [nombre, calificacion1, calificacion2, calificacion3]
                calificaciones.append(alumno)
                promedios.append(promedioT)
                alumnos += 1 
            elif confirmacion == '2' :
                print ('Por favor, ingrese la calificación correcta del alumno.')
                continue
            else :
                print ('Se ha ingresado una opción no válida.')
                continue
        elif calificacion1 <= 10 :
            if calificacion2 == 0 :
                pass
            elif calificacion2 <= 10 :
                if calificacion3 == 0 :
                    pass
                elif calificacion3 <= 10 :
                    promedio = ((calificacion1 + calificacion2 + calificacion3) // no_calificaciones)
                    promedioT = [nombre, promedio]
                    alumno = [nombre, calificacion1, calificacion2, calificacion3]
                    calificaciones.append(alumno)
                    promedios.append (promedioT)
                    alumnos += 1 
                else :
                    print ('Se ha ingresado un opción no válida.')
                    continue
            else :
                print ('Se ha ingresado una opción no válida.')
                continue
        else : 
            print ('Se ha ingresado una opción no válida.')
            continue
    elif opcion == '2':
         print (f'El programa ha terminado con {alumnos} alumnos.')
         break
    else :
        print ('Se ha ingresado una opción no válida.')
        continue

print ('¿Desea revisar las calificaciones ingresadas?')
comprobacion = input ('Sí [1] o No [2]: ')

if comprobacion == '1' :
    print ('Las calificaciones de los alumnos son:')
    print (calificaciones)
    print ('¿Desea ver la lista de promedios?')
    decision = input ('Sí [1] o No [2]: ')
    if decision == '1':
        print('Los promedios por alumno son:')
        print (promedios)
    elif decision == '2':
        exit ()

elif comprobacion == '2':
    print (promedios)
    exit ()

else:
    print ('La opción ingresada no es válida, pero aún así se presentarán los promedios')
    print (promedios)
    exit ()