'''Comparación de Números 
Descripción: Escribe un programa 
que solicite al usuario dos números 
y determine cuál es mayor, menor o 
si son iguales.'''

while True:
    print('comparacion de numeros:\n')
    numOne=int(input('ingresa el primer numero:'))
    numtwo=int(input('ingresa el segundo numero:'))
    if numOne>numtwo:
        print('el numero mayor es:',numOne)
    elif numOne<numtwo:
        print('el numero mayor es:', numtwo)
    else:
        print('los numeros son iguales')
    volver=input('\nvolver al inicio? 1)si 2)no\n :')
    if volver !='1':
        print('fin del programa hasta luego :p')
        break