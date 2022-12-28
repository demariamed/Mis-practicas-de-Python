# Modulo m_factorial(m_factorial2.py)

"""  Modulo que contiene la funcion recursiva del factorial"""

def factorial(num) :
    """ Calcular el factorial de un numero. """

    if num == 0 :
        return 1
    else :
        return num * factorial(num -1)

print(__name__) # Imprime la variable 

if __name__=="__main__" : # Condicional para ver si la variable es main y si se ejecuta con el programa principal
    import sys # 'sys' es un modulo que permite acceder a parametros y funciones especificas del sistema
    print (factorial(int(sys.argv[2]))) # Impresion del resultado de la funcion factorial tomando como parametro un numero ingresado al ejecutar nuestro programa desde la terminal

        