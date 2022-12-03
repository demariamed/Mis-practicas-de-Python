# Solicitud de año

entrada = input("¡Hola! Introduce año actual:")
año = 2022

if entrada.isnumeric() :
    año = int(entrada)
else :
    print("Dato incorrecto. Debes introducir un numero")
    exit()

if año <= 0 :
    print("¡ERROR! Ese año ha caducado")
elif año > 2022 :
    print("Todavia no ha ocurrido ese año")
elif año < 2022 :
    print("Año caducado. Introduce año actual")
else :
    print("Espacio y tiempo correctos.¡Felicidades!")

