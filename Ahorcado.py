import os

print('Juego del Ahorcado (para dos jugadores)\n\n' + 
'El objetivo del juego es que el jugador 1 introduzca una palabra y\n' +
'el jugador 2 la adivine antes de completar el AHORCADO.\n' +
'Por cada fallo se sumará una letra de AHORCADO, lo que le da un margen de \n' +
'8 intentos al jugador 2.\n' +
'Al cumplir los 8 intentos, si no se ha adivinado la palabra,\n' +
'el jugador 1 gana la partida. Si se adivina la palabra antes de\n' + 
'completar el AHORCADO el jugador 2 gana la partida.')


palabra = input("Que el jugador Número 1 introduzca una palabra: ")
palabra_lista = []
for p in palabra:
    palabra_lista.append(p)
    
input('\nPulse ENTER para continuar...')
os.system('cls')


print('Turno del jugador 2\n\n')


respuesta = []
for r in palabra_lista:
    respuesta.append('_')
print(f'Palabra del Jugador 1: {respuesta}')


ahorcado = ['A','H','O','R','C','A','D','O']
vidas = ['_','_','_','_','_','_','_','_']
print(f'\nVidas del Jugador 2: {vidas}')

contador = 0 

# TODO: hay que buscar como salir del bucle cuando se aciertan todas las letras o cuando se completa el ahorcado

for i in range(len(vidas) + len(palabra_lista)): 
    letra = input('\nIntroduzca una letra: \n')
    if letra in palabra_lista:
        respuesta[palabra_lista.index(letra)] = letra  # TODO: y si hay letras repetidas???????????
    else:
        vidas[contador] = ahorcado[contador]   
        contador += 1 
    print(f'Palabra del Jugardor 1: {respuesta}') 
    print(f'Vidas del Jugador 2: {vidas}')   