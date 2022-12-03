#haremos un diccionario, las llaves seran las palabras y los valores seran los emojis
emoji_diccionario = {"feliz":"😀", "amo":"😍", "risa":"🤣", "sonrisa":"😊", "llorar":"😭","beso":"😘", \
    "aplauso":"👏","reir":"😁","fuego":"🔥","roto":"💔","pensando":"🤔", \
        "maravillado":"🤩","aburrido":"🙄","guiño":"😉","ok":"👌","abrazo":"🤗", \
            "cool":"😎","enojado":"😠","python":"🐍"} 
frase = input('Escribe una frase: ')
frase = frase.lower() #Especificando que solo queremos minusculas
palabras = frase.split() #El metodo split divide las palabras por espacios que ingresa el usuario y los guarda como elementos en una lista
print(palabras)

respuesta = ''

for palabra in palabras:
    if palabra in emoji_diccionario:
        respuesta = respuesta + emoji_diccionario[palabra] + ' ' #Concatenacion de un espacio al final de cada palabra ingresada
    else:
        respuesta = respuesta + palabra + ' ' #Concatenacion de un espacio al final de cada palabra ingresada

print(respuesta)

