#Probando ambitos

titulo = 'Probando ambitos'
suma = 10.5

def sumar():
    suma = 2+2
    print('Suma en ambito local', suma,id(suma))

print('Antes de llamar a la funcion')
print('Suma del ambito global',suma,id(suma))
sumar()
print('Despues de llamar a la funcion sumar')
print('Suma del ambito global',suma,id(suma))
