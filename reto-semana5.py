entrada = input("¡Hola! Introduce tu edad: ")

edad = 0

if entrada.isnumeric() :
    edad = int(entrada) 
else :
    print("Dato incorrecto. Debes introducir un numero")
    exit()

if edad <= 0:
    print("WOOOWWW!! Que joven eres. Pero, lo siento, eso no es posible")
elif edad > 115 :
    print("VAYA!!!! ¿Como le haces para vivir tanto? No te creo, mejor intenta de nuevo")
elif edad <18 :
    print("Eres menor de edad asi que no puedes comprar tu cigarro")
else : 
    print("Eres mayor de edad. Aqui tienes tu cigarro")
