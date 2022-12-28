import m_alumnos as m3 # Importando el modulo de alumnos y asignando alias m3

numero_alumnos = input("¿Cuantos alumnos desea registrar?: ") # Declarando la variable numero_alumnos y se solicita al usuario uan respuesta

if numero_alumnos.isdigit() : # Declarando una condicional, si el numero_alumnos es un digito se jecuta la accion
    numero_alumnos = int(numero_alumnos) 
    m3.captura_alumnos(numero_alumnos)
else : 
    m3.captura_alumnos() # Si no llegara a ser un numero llamamos a m3 para que capture los datos

    