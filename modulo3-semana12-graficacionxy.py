# Generacion de un grafico de dispersion con la funcion 'scatter'

import random 
import matplotlib.pyplot as plt

eje_x = [random.randint(1,100) for n in range (100)] # Lista de 100 elementos en una sola linea para generar datos aleatorios entre el 1 y el 100 para el eje x

eje_y = [random.randint(1,100) for n in range (100)]

plt.scatter(eje_x, eje_y) # Para posicionar y que hagan correlacion los ejes x y y 

plt.title("Grafica de dispersion") # Funcion 'title' para agregar titulo a la grafica o una cadena de caracteres 

plt.show() # Funcion 'show' para generar un vistograma
