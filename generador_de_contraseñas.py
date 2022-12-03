# Programa que genera una contraseña de 8 caracteres a partir de 3 palabras dadas por el usuario

palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")
palabra3 = input("Introduce la tercera palabra: ")
#Si la palabra es de menos de 2 caracteres, se rellena con X  
if len(palabra1) < 2:
    palabra1 = "X" + palabra1
if len(palabra2) < 2:
    palabra2 = "X" + palabra2
if len(palabra3) < 2:
    palabra3 = "X" + palabra3
#Se genera la contraseña
contraseña = palabra1[0] + palabra2[0] + palabra3[0] + palabra1[1] + palabra2[1] + palabra3[1]
print("La contraseña es:", contraseña)

# Se solicita contraseña al usuario
# Si la contraseña es de menos caracteres informa cuántos faltan
# Si la contraseña es de más caracteres informa cuántos sobran
# Si la contraseña es correcta, informa que es correcta

contraseña_usuario = input("Introduce la contraseña: ") # Se solicita contraseña al usuario
if len(contraseña_usuario) < len(contraseña):
    print("Faltan", len(contraseña) - len(contraseña_usuario), "caracteres")
elif len(contraseña_usuario) > len(contraseña):
    print("Sobran", len(contraseña_usuario) - len(contraseña), "caracteres")
elif contraseña_usuario == contraseña:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
