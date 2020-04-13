

#No se usan llaves ni parentesis
#Con espacios para respetar la condicion
calificacion=float(input('Cual es tu calificacion?'))
puntos_extras=True
#Falsy: None False 0, String vacio
#Truthy: String con valor
#Truthy o Falsy
if calificacion>=7:
    print('Ya pasaste')
elif calificacion>=5 and calificacion<6:
    print('Si te rifas con un pomo, pasas')
#elif calificacion==6 or puntos_extras:
#    print('Chanse y pasas')
else:
    print('Ya ni vengas')