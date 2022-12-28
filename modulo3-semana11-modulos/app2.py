# Ejemplo de importacion de la funcion en un modulo dado

from m_area import area as a 

# Sentencia 'from' para especificar los objetos de los cuales se va a hacer uso en este caso un area

area = a(figura="Triangulo", base=10, altura=8) # Estableciendo parametros 

print("El area del triangulo 10, 8 es: ", area) #Impresion del valor 'area'