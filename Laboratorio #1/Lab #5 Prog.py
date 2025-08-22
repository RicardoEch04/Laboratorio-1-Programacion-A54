'''Ejercicio 5: Calculadora de Descuento 
Descripción: Escribe un programa 
que solicite al usuario el precio de un 
producto y el porcentaje de 
descuento, y calcule el precio final 
después del descuento. '''

while True:
    print('\ncalculadora de descuento\n')
    
    x=int(input('ingresa el costo del producto\n: '))
    y=int(input('ahora ingresa el porcentaje de descuento\n : '))
    print(f'el precio final es de: {(x-(x*y)/(100))}\n')
    volver= int(input('volver al inicio? 1)si 2)no \n:'))
    if volver !=1:
        print('cerrando programa')
        break