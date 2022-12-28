# Generando una distribución gauss para analisis de comportamiento

import numpy as np
import  matplotlib.pyplot as plt # Importar el modulo pyplot que es el que nos permite graficar o trazar los valores

datos = np.random.normal(0,1.0,1000) # Generacion de 1000 muestras de una distribucion normal con una desviacion estandar de 0.1 y una media de 0 
 
# Podriamos decir que si tenemos la calificacion de 1000 alumnnos, tomara una muestra aleatoria de 1000 calificaciones para saber el comportamiento general de las calificaciones

plt.hist(datos) # Funcion 'hist' para imprimir los datos 
plt.show() # Funcion 'show' para generar un vistograma
