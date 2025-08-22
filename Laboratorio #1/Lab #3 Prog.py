'''Ejercicio 3: Determinar Par o Impar 
Descripción: Escribe un programa 
que solicite al usuario un número y 
determine si es par o impar.'''

while True:
    numOne=int(input('ingresa el numero para determinar si es par o impar: \n'))
    if numOne%2==0:
        print(f'el numero "{numOne}" es par')
    else:
        print(f'el numero "{numOne}" es impar')
    volver=input('volver al inicio? \n 1)si 2)no \n ')
    if volver !='1':
        print('fin del programa')
        break  