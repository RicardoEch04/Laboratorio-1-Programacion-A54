'''Ejercicio 4: Clasificación de Edad 
Descripción: Escribe un programa 
que solicite al usuario su edad y 
determine si es un niño (menor de 12 
años), adolescente (menos de 18), 
adulto (menos de 60) o adulto mayor 
(60 o más).'''

while True:
    print('clasificacion de edad\n')
    x=int(input('ingrese su edad: '))
    if x<=12:
        print('es un niño menor de edad')
    elif x>12 and x<=18:
        print('es un adolecente')
    elif x>=18 and x<60:
        print('es un adulto')
    elif x>60:
        print('es un adulto mayor')
    else:
        print('ingresa una edad valida')
    volver=int(input('\nvolver al inicio? 1)si 2)no\n:'))
    if volver !=1:
        print('finalizando programa hasta luego :D')
        break
