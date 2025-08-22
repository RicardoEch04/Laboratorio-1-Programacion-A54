'''Ejercicio 6: Conversión de 
Temperaturas 
Descripción: Escribe un programa 
que convierta una temperatura dada 
en grados Celsius a grados 
Fahrenheit y Kelvin.'''
while True:
    print('\nconversion de temperaturas\n')
    c=float(input('ingresa la temperatura en grados celsius:\n'))
    print(f'\nen Fahrenheit son: {((c*9/5)+32)} y en Kelvin son: {c+273.15}')
    volver=int(input('\nvolver al inicio? 1)si 2)no \n'))
    if volver != 1:
            print('cerrando programa')
            break