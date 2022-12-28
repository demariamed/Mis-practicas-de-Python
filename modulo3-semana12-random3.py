# # modulo3-semana12.random3.py

# import numpy as np

# numeros = np.random.rand()

# print(numeros)

# # NO GENERO NUMERO ALEATORIO ENTRE EL 0 Y EL 1 
# # ModuleNotFoundError: No module named 'numpy'

# # Problema solucionado en terminal a traves de (pip3.10 install numpy) y (python3 -m pip install numpy)

##########################################

# # Numero aleatorio con una salida constante

# import numpy as np

# np.random.seed (0) 
# numeros = np.random.rand()

# print(numeros)

############################################

# Lista de 5 numeros pseudoaleatorios

import numpy as np

np.random.seed (0) 
numeros = np.random.rand(5)

print(numeros)
