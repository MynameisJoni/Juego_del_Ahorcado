import os

print('Juego del Ahorcado (para dos jugadores)\n\n' + 
'El objetivo del juego es que el jugador 1 introduzca una palabra y\n' +
'el jugador 2 la adivine antes de completar el AHORCADO.\n' +
'Por cada fallo se sumará una letra de AHORCADO, lo que le da un margen de \n' +
'8 intentos al jugador 2.\n' +
'Al cumplir los 8 intentos, si no se ha adivinado la palabra,\n' +
'el jugador 1 gana la partida. Si se adivina la palabra antes de\n' + 
'completar el AHORCADO el jugador 2 gana la partida.\n')


palabra = input("Que el jugador Número 1 introduzca una palabra: ")
palabra_lista = []
for p in palabra:
    palabra_lista.append(p.upper())
    
input('\nPulse ENTER para continuar...')
os.system('cls') # 'cls' -> 'clear' en macOS


print('Turno del jugador 2\n\n')


respuesta = []
for r in palabra_lista:
    respuesta.append('_')
print(f'Palabra del Jugador 1: {respuesta}')


ahorcado = ['A','H','O','R','C','A','D','O']
vidas = ['_','_','_','_','_','_','_','_']
print(f'\nVidas del Jugador 2: {vidas}')

contador = 0 

for i in range(len(vidas) + len(palabra_lista)): 
    letra = input('\nIntroduzca una letra: \n').upper()
    for i, n in enumerate(palabra_lista):
        if letra == n:
            respuesta[i] = letra.upper() 
    if letra not in palabra_lista:
        vidas[contador] = ahorcado[contador]   
        contador += 1
    print(f'\nPalabra del Jugardor 1: {respuesta}\n') 
    print(f'Vidas del Jugador 2: {vidas}\n')
    if respuesta == palabra_lista:
        print(f'Palabra "{palabra}" adivinada! El Jugador 2 ha ganado la partida!!\n')
        break
    elif vidas == ahorcado:
        print(f'Ahorcado completado... El Jugador 1 ha ganado la partida!!\n')   
        break  
