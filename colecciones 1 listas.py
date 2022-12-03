# mix = [0, 1.0, "dos", 3 + 4j]

# for i in mix :
#     print(f"{i:6} - Tipo: {type(i)}")

# A continuación, impresión para determinar el tamaño de la lista con función “len”.
# print(len(mix))

# Declaracion 
# sin_dos = mix[:2] + mix[3:]
# print(mix, sin_dos)

# Duplicacion
# duplicado = mix * 2
# print(duplicado)

# Cuadrados

# cuadrados = [0,1,4,9,16,25]
# for i in range(len(cuadrados)) :
#     print(f"{i}**2 = {cuadrados[i]}")

# cuadrados = [0,1,4,9,16,25]
# for i in range(len(cuadrados)) :
#     cuadrados [i] = cuadrados [i] * i
#     print(f"Ahora estan al cubo {cuadrados[i]}")

# Para añadir o eliminar elmentos

cuadrados = [0,1,4,9,16,25]
for i in range(len(cuadrados)) :
    cuadrados [i] = cuadrados [i] * i
    print(f"Ahora estan al cubo {cuadrados[i]}")

cuadrados.append(7 ** 3)

# Para insertar un elemento en la posicion señalada

cuadrados.insert(6,6 ** 3)

# Para agregar multiples valores al final de la lista

cuadrados.extend([27, 1000, -1])

# Para agregar un rango de numero 
cuadrados.extend(range(-1, -4, -1))

# Eliminar uno o varios elementos de la lista por medio de indices o slicing (dividiendo)
del cuadrados[9:]

# Eliminacion de primer valor de coincidencia de izquierda a derecha
cuadrados.remove(27)

print(cuadrados)

# Remove busca un valor y pop los busca por medio de indices y devuelve el resultado extraido 
valor_removido = cuadrados.pop(2)

print(valor_removido)

print(cuadrados)

# Elimina todos los elementos de una lista
cuadrados.clear()

print(cuadrados)