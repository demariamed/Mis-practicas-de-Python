tiempos = {
    'Hamilton': '1:49.8',
    'Bottas': '1:56.4',
    'Perez': '1:53.8',
    'Verstappen': '1:52.6' #sin coma para indicar que aqui se acaba el diccionario
}

# items nos permite devolver una lista de tuplas obteniendo la llave de un respectivo valor

print(tiempos.items())

# keys devuelve una lista con todas las llaves usadas en el dicionario

print(tiempos.keys())

# values duevlve una lista con todos los valores del diccionario

print(tiempos.values())

# regresar el valor de una llave

print(tiempos.get('Hamilton'))

print(tiempos.get('hamilton','No encontrado'))