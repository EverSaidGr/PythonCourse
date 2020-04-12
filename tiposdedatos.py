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

print ('Multiplicacion')
num1_multi=float (input('Ingresa el primer valor'))
num2_multi=float (input('Ingresa el segundo valor'))

Total_multi=num1_multi*num2_multi
print('El total de la multi es de: ','{:0.3f}'.format(Total_multi))