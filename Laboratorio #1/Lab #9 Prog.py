'''Ejercicio 9: Calculadora de Promedio 
Descripción: Escribe un programa 
que solicite al usuario tres 
calificaciones y calcule el promedio.'''

while True:
    while True:
        print('\ncalculadora de promedio:\n')
        Cone= float(input('ingrese la primera calificacion\n: '))
        Ctwo= float(input('ingrese la segunda calificacion\n: '))
        Cthre=float(input('ingrese la tercera calificacion\n: '))
        print(f'el promedio de las calificaciones es: {round((Cone+Ctwo+Cthre)/3, 2)}')
        volver= input('desea volver a intentarlo? 1)si 2)no\n: ')
        if volver !='1':
            print('cerrando programa, hasta luego')
            break