from random import randint

jugador=int(input('Que arma escoger?(1)Piedra (2)Papel (3)Tijeras'))

numero_aleatorio=randint(1,3)
print(numero_aleatorio)
if numero_aleatorio==1:
    print('Computadora: Piedra')
elif numero_aleatorio==2:
    print('Computadora: Papel')
else:
    print('Computadora: Tijera')

#Piedra
if jugador==1 and numero_aleatorio==1:
    print('Empate')
elif jugador==1 and numero_aleatorio==2:
    print('Gano la computadora')
elif jugador==1 and numero_aleatorio==3:
    print('Gano el usuario')

#Papel
elif jugador==2 and numero_aleatorio==2:
    print('Empate')
elif jugador==2 and numero_aleatorio==3:
    print('Gano la computadora')
elif jugador==2 and numero_aleatorio==1:
    print('Gano el usuario')

#Tijera
elif jugador==3 and numero_aleatorio==3:
    print('Empate')
elif jugador==3 and numero_aleatorio==1:
    print('Gano la computadora')
elif jugador==3 and numero_aleatorio==2:
    print('Gano el usuario')

else:
    print('Da un numero en el rango')