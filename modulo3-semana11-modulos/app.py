#Ejemplo de importacion de un modulo completo, con todos sus nombres definidos

import m_factorial2 as mf  
# Sentencia import para incluir modulos en nuevos codigos sin terminacion .py con alias 'mf' 
# 'as' para asignar un alias

fact5 = mf.factorial(5) # Declarando una variable y anteponiendo el nombre del modulo seguido de la funcion a emplear

print(f"El factorial de 5 es: {fact5}") # Impresion del factorial y concatenacion de la variable


# No tenemos el código del calculo del factorial en este archivo, pero lo estamos mandando a llamar de la función que declaramos en el modulo m_factorial.py