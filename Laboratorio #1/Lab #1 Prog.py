"""Ejercicio 1: Calculadora Básica 
Descripción: Escribe un programa que solicite al usuario dos números enteros y realice las 
operaciones aritméticas básicas (suma, resta, multiplicación, división, división de 
piso y residuo) entre ellos. Muestra los resultados en pantalla."""

while True:
    print('calculadora basica')
    numEnt=int(input('ingrese el primer numero (entero): '))
    numtwo=int(input('ingrese el segundo numero entero: '))
    x=input('\nque operacion desea realizar? \n1) suma \n2) resta \n3) multiplicacion \n4) division \n5) division de piso \n6) residuo \n:')
    if x=='1':
        print(f'la suma es: {numEnt + numtwo}')
    elif x=='2':
        print(f'la resta es: {numEnt - numtwo}')
    elif x=='3':
        print(f'la multiplicacion es: {numEnt*numtwo}')
    elif x=='4':
        print(f'la division es: {numEnt/numtwo}')
    elif x=='5':
        print(f'la division de piso es: {numEnt//numtwo}')
    elif x=='6':
        print(f'el residuo es: {numEnt%numtwo}')
    else:
        print('opcion no valida (solo numeros enteros)')
    volver= input('\nvolver al inicio? 1)si 2)no\n :')
    if volver !='1': 
        print('fin del programa hasta luego :D')
        break

