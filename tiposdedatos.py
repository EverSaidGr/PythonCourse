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

#print('El valor de tu suma es: ',suma)
print('Ingresa los numero a realizar la suma')
numero_1=float (input ('Ingresa el primer valor: '))
numero_2=float(input('Ingresa el segundo valor: '))
total=numero_1+numero_2
print('Total de la suma es de:','{:0.2f}'.format(total))
#
#Resta
#
print('Resta')
numero_1=float (input ('Ingresa el primer valor: '))
numero_2=float(input('Ingresa el segundo valor: '))
total=numero_1-numero_2
print('Total de la resta es de:','{:0.2f}'.format(total))

#
#Multipliaciacion 
#
print ('Multiplicacion')
num1_multi=float (input('Ingresa el primer valor'))
num2_multi=float (input('Ingresa el segundo valor'))

Total_multi=num1_multi*num2_multi
print('El total de la multi es de: ','{:0.3f}'.format(Total_multi))
#
#Division
#
print('Division ')
num1_div=float(input('Da el divisor'))
num2_div=float(input('Da el dividendo'))
total_Divi=num1_div/num2_div
print('El resultado de la division es:','{:0.3f}'.format(total_Divi))
#
#Division exacta
#
print('Division exacta')
num1_DivEx=float (input('Da el divisor'))
num2_DivEx=float (input('Da el dividendo'))
total_DivEx= num1_DivEx//num2_DivEx
print('El resultado de la division es:','{:0.3f}'.format(total_DivEx))
#
#Modulo
#
print('Modulo')
num1_mod=float(input('Da el primer numero'))
num2_mod=float(input('Da el segundo numero'))
total_Mod=num1_mod%num2_mod
print('El total de modulo es: ','{:0.3f}'.format(total_Mod))
#
#Potencia
#
print('Modulo')
num1_mod=float(input('Da el numero a base'))
num2_mod=float(input('Da el exponente'))
total_Mod=num1_mod**num2_mod
print('El total de la potencia es: ','{:0.3f}'.format(total_Mod))