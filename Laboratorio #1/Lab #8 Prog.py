'''Ejercicio 8: Calculadora de Año 
Bisiesto 
Descripción: Escribe un programa 
que determine si un año dado es 
bisiesto o no. Un año es bisiesto si es 
divisible por 4, pero no por 100, a 
menos que también sea divisible por 
400. '''
while True:
    print('\ncalculadora de año bisiesto\n')
    año=int(input('ingresa el año a evaluar: \n'))
    if año%4==0 and año%100!=0 or año%400==0:
        print(f'el año {año} es bisiesto')
    else:
        print(f'el año {año} no es bisiesto')
    volver=input('desea volver a intentar con otro año?  1)si  2)no\n')
    if volver != '1':
        print('cerrando programa')
        break
