# Definir una funcion para construir la grafica
# Definir un diccionario con las calificaciones del alumno
# Pedir al alumno el nombre del alumno
# Mandar a llamar a la grafica y mostrarla


import  matplotlib.pyplot as plt 

def diagrama_barras_calificaciones(notas, color, alumno) :
    """
    Dibujar la grafica de barras con las calificaciones
    """
    plt.bar(notas.keys(), notas.values(), color=color)
    plt.title('Calificaciones de:' + alumno)

calificaciones = {
    'Programacion': 9,
    'Español' : 6.5,
    'Calculo': 4,
    'Historia': 8,
    'Biologia': 10,
    'Ingles': 7
}

alumno = input("Nombre del alumno:")
diagrama_barras_calificaciones(calificaciones, 'green', alumno)
plt.show() 