#string='Hola, mundo'#Cadena de valores
string=input('Escribe un mensaje: ')

#Inidces caracteres
primer_letra=string[0]#Ver que letra esta en la posicion 0(Cuenta inicia desde 0)
longitud=len(string)#Calcular la longitud de una cadena da valores
ultimo_valor=string[longitud-1]
string[-1]
print(ultimo_valor)


# Slices 
#Una rebanada o parte de la cadena
mensaje='Estoy aprendiendo a programar python'
slicito_1 = mensaje[12:]#Regresame todo lo que este despues del indice 12
slicito_2 =mensaje[:21]#Regresame todo lo que este antes del indice 12
slicito_3 = mensaje [6:17]
print(slicito_1)
print(slicito_2)
print(slicito_3)

#Split
#Separa
splited=mensaje.split(' ')#Separa cada que encuentre un "espacio"
print (splited[1])#Listas 
print (splited)
print (splited[1])#Listas 

#Listas

lista=['palabra',3,3.5, True,['soy','otra','lista']]

print(lista[4][1])#Acceder a una lista anidada

lista_anidada=lista[4]#Acceder primero a la posicion de la lista
print(lista_anidada[1])

#Quitar el ultimo elemento

print(lista)
nueva_lista=lista.pop()#Que quite de la lista el ultimo elemento
print(nueva_lista)
print(lista)

#Agregar elemento
lista.append(False)
print(lista)

#Join
#Toma una lista de string y convierte a un string

lista_string=['1','2','3','4']
separador='-'
lista_joineada=separador.join(lista_string)
print(lista_joineada)