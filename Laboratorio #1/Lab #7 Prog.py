'''Ejercicio 7: Calculadora de IMC 
Descripción: Escribe un programa 
que calcule el Índice de Masa 
Corporal (IMC) de una persona, 
dado su peso y altura. El IMC se 
calcula con la fórmula:'''
while True:
    print('calculadora de IMC (indice de masa corporal)\n')
    h=float(input('ingrese la altura en metros: '))
    p=float(input('ingrese el peso en kg: '))
    print(f'\nel IMC es: {round((p/h**2), 1)}\n')
    volver=int(input('desea volver a intentarlo? 1)si 2)no)\n :'))
    if volver !=1:
            print('\n \ncerrando programa bye')
            break
