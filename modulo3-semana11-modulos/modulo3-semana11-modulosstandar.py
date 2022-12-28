import sys
print(sys.path) # Muestra todos los directorios para la busqueda de un modulo

sys.path.append('XXXXXXX') # Si decidimos guardar nuestro modulo en algun directorio diferente a los listados podemos agregarlo por medio de append seguido de la ruta del archivo

print(sys.path) #Imprime nuevamente la lista de los directorios de busqueda

import m_factorial2 # Impresion del modulo

print(dir(m_factorial2)) # dir imprime el contenido del modulo

print(dir(sys)) # dir imprime el contenido del modulo



