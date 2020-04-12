nombre='Ever'
#print('Hola'+nombre)
#Tipos de datos
entero=15
flotantes=5.323232
string= 'Texto'
booleano = True
#Operadores aritmeticos
suma=4+5
resta=5-2
multiplicacion =5*4
potencia= 5**2
division =10/2
division_exacta =5//2
modulo=10%2

numero_1=float (input ('Ingresa el primer valor: '))
numero_2=float(input('Ingresa el segundo valor: '))

#print('El valor de tu suma es: ',suma)
print('Suma')

total=numero_1+numero_2
print('Total de la suma es de:','{:0.2f}'.format(total))
#
#Resta
#
print('Resta')

total=numero_1-numero_2
print('Total de la resta es de:','{:0.2f}'.format(total))

#
#Multipliaciacion 
#
print ('Multiplicacion')
Total_multi=numero_1*numero_2
print('El total de la multi es de: ','{:0.3f}'.format(Total_multi))
#
#Division
#
print('Division ')

total_Divi=numero_1/numero_2
print('El resultado de la division es:','{:0.3f}'.format(total_Divi))
#
#Division exacta
#
print('Division exacta')

total_DivEx= numero_1//numero_2
print('El resultado de la division es:','{:0.3f}'.format(total_DivEx))
#
#Modulo
#
print('Modulo')

total_Mod=numero_1%numero_2
print('El total de modulo es: ','{:0.3f}'.format(total_Mod))
#
#Potencia
#
print('Modulo')

total_Mod=numero_1**numero_2
print('El total de la potencia es: ','{:0.3f}'.format(total_Mod))