#4/3 pi*r**3
import math
print('Volumen de una esfera')

radio=float(input('Ingresa el radio de la esfera en cm: '))

#print('El valor de pi es de: ',math.pi)

Volumen=(4/3 * math.pi)*(radio**3)

print('El volumen de la esfera es de: ', '{:0.2f}'.format(Volumen),'cm3')