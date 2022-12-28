# Numero aleatorio con una salida constante y graficacion 

import numpy as np
import  matplotlib.pyplot as plt # Importar el modulo pyplot que es el que nos permite graficar o trazar los valores

np.random.seed (0)

numeros = np.random.rand(15)

print(numeros)

plt.plot(numeros) # Mandar a llamar la funcion plt
plt.show() # Escribir funcion 'show' para mostrar la grafica

