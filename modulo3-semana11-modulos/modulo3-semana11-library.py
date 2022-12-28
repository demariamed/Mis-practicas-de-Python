# library1.modulo1 # Definiendo el modulo 1 que se encuentra dentro de la library1


import numpy as np

a = np.arange(6)

a2 = a[np.newaxis, :]

print(a2.shape)
