'''Ejercicio 10: Calculadora de Área 
de un Triángulo 
Descripción: Escribe un programa 
que calcule el área de un triángulo, 
dados su base y altura.'''

while True:
        print('\ncalculadora de area de un triangulo:\n')
        h=int(input('ingrese la altura del triangulo:\n '))
        b=int(input('ingrese la base del triangulo:\n '))
        print(f'el area del triangulo es: {(b*h)/2}')
        volver= input('\ndesea volver a intentarlo? 1)si 2)no\n:')
        if volver !='1' and volver!='si':
            print('cerrando programa')
            break
    