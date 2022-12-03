# Traductor 

diccionario_aleman = {'rojo' : 'rot', 'naranja' : 'orange', 'amarillo' : 'gelb', \
    'verde' : 'grün', 'azul' : 'blau', 'violeta' : 'violett'}

diccionario_hebreo = {'rojo' : 'adom', 'naranja' : 'catom', 'amarillo' : 'tzaov', \
    'verde' : 'yarok', 'azul' : 'kahol', 'violeta' : 'sagol'}

print ('Bienvenido al traductor de colores. Los idiomas disponibles son: aleman y hebreo')
idioma = input('Indique el idioma al que quiere traducir: ')
idioma = idioma.lower()
if idioma == 'aleman' :
    texto = input ('Ingrese su palabra: ')
    texto = texto.lower()
    palabras = texto.split()
    traduccion = ''
    for palabra in palabras:
        if palabra in diccionario_aleman:
            traduccion = traduccion + diccionario_aleman[palabra] + ' '
        else :
            traduccion = traduccion + palabra + ' '
    print (traduccion)

elif idioma == 'hebreo' :
    texto = input ('Ingrese su palabra: ')
    texto = texto.lower()
    palabras = texto.split()
    traduccion = ''
    for palabra in palabras:
        if palabra in diccionario_hebreo:
            traduccion = traduccion + diccionario_hebreo[palabra] + ' '
        else:
            traduccion = traduccion + palabra + ' '
    print(traduccion)
    
else:
    print('Idioma no disponible. Por favor inténtelo de nuevo.')
    exit()