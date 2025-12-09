####################################################

# Autor: Ander Lifeng Sola
# Alias: Tupanditta :)
# Color Favorito: Azul Stich

# Fecha: Jv 04/12/2025
# Archivo: JUEGO_HartzaiJokua_1.1.py
# Descripción: Conecta 4.

####################################################


################################            FUNCIONES

#####       1. Crear y mostrar tabla

def crear_tabla(dimensiones):
    tablero = []
    fila_numeros = []

    for numero in range(dimensiones):
        fila_numeros.append(numero) #creo una fila de números
    tablero.append(fila_numeros)

    for fila in range(dimensiones):
        lista_fila = []

        for columna in range(dimensiones):
            lista_fila.append('*')
        tablero.append(lista_fila)

    return tablero #Devuelve un tablero NxN lleno de '*'

def mostrar_tabla(tablero): 
    #Cuerpo General
    print(' _^_'*(len(tablero)-1))

    for fila in range(len(tablero)):
        print('|', end=' ')

        for elemento in range(len(tablero)-1):
            print(tablero[fila][elemento], end=' | ')

        print()     

#####       2. Movimiento y colocar fichas

def colocar_ficha(columna, jugador, tablero):
    #Variables
    ficha = ''
    ultimo_vacio = 1

    #Cuerpo General
    if jugador == '1': 
        ficha = 'X' 
    else:
        ficha = 'O' 

    # IMPORTANTE: Empezamos en range 1, no 2. La fila 1 también se juega.
    for fila in range(1, len(tablero)):
        if tablero[fila][columna] == '*':
            ultimo_vacio = fila
            # Si es la ultima fila del todo (el suelo), la ponemos ahí
            if fila == (len(tablero) - 1): 
                tablero[ultimo_vacio][columna] = ficha

        else:
            # Si encontramos una ocupada, ponemos en la anterior (ultimo_vacio)
            tablero[ultimo_vacio][columna] = ficha
            break #Ya he añadido la nueva ficha, termino el bucle
    
    return tablero

def movimiento_valido(columna, tablero): #No se puede añadir una ficha en una columna llena de fichas
    #Variables
    valido = True
    ancho_tablero = len(tablero) - 1

    # Comprobamos que la columna exista (mayor que 0 y menor que el ancho)
    if columna < 0 or columna >= ancho_tablero:
        valido = False
    
    # Comprobamos que no esté llena (mirando la fila 1, que es la superior de juego)
    elif tablero[1][columna] != '*':
        valido = False

    return valido #Booleano que dice si hay sitio en la columna para una ficha más

#####       3. Analizar tablero

def comprobar_tabla(tablero, jugador): 
    #Variables
    ficha = ''
    terminado = False

    #Cuerpo General
    if jugador == '1':
        ficha = 'X' #Asigno diferentes fichas a los diferentes jugadores

    else:
        ficha = 'O' #Asigno diferentes fichas a los diferentes jugadores
    
    #Columnas
    for columna in range(len(tablero)-1): 
        cont = 0
        for fila in range(1, len(tablero)): 
            if tablero[fila][columna] == ficha:
                cont += 1
                if cont == 4:
                    terminado = True
                    break
            else:
                cont = 0
        if terminado: #Si ya ha ganado, salimos
            break

    #Filas
    if not terminado: #Solo compruebo filas si ya he comprobado columnas

        for fila in range(1, len(tablero)): 
            cont = 0
            for columna in range(len(tablero)-1): 
                if tablero[fila][columna] == ficha:
                    cont += 1
                    if cont == 4:
                        terminado = True
                        break
                else:
                    cont = 0
            if terminado: #Si ya ha ganado, salimos
                break

    #Diagonal
    if not terminado: #Solo compruebo diagonal si ya he comprobado filas y columnas

        #Diagonal Descendiente
        for fila in range(1, len(tablero)-3):
            for columna in range((len(tablero) - 1) - 3):
                if tablero[fila][columna] == ficha:
                    if tablero[fila+1][columna+1] == ficha and tablero[fila+2][columna+2] == ficha and tablero[fila+3][columna+3] == ficha:
                        terminado = True
                        break
            if terminado: break

        #Diagonal Ascendiente
        if not terminado: #Solo si no ha ganado ya
            for fila in range(1, len(tablero)-3):
                for columna in range(3, (len(tablero) - 1)):
                    if tablero[fila][columna] == ficha:
                        if tablero[fila+1][columna-1] == ficha and tablero[fila+2][columna-2] == ficha and tablero[fila+3][columna-3] == ficha:
                            terminado = True
                            break
                if terminado: break

    return terminado #Booleano que dice si el juego ha terminado o no

def tabla_llena(tablero):
    terminado = True #Supongo que el tablero está lleno

    for fila in range(1, len(tablero)):
        if '*' in tablero[fila]:
            terminado = False #Con que haya un solo hueco vacío, quiere decir que el tablero no está lleno

    return terminado #Booleano que me dice si está lleno o no el tablero


################################            FUNCIÓN GENERAL
def HartzaiJokua():

    #####   Variables
    terminado = False #Comienzo con False hasta que el juego termine; algún jugador conecta 4 fichas, o la tabla se llena

    jugador_1 = 0 #Guardo la columna en la que el jugador quiere añadir una ficha
    jugador_2 = 0 #Guardo la columna en la que el jugador quiere añadir una ficha

    #####   Llamar Funciones
    dimensiones = int(input("Introduzca un número entero para las dimensiones del tablero: "))
    
    while dimensiones < 4:
        print('Las dimensiones del tablero deben der 3 o más, introduzca de nuevo las dimensiones')
        dimensiones = int(input("Introduzca un número entero para las dimensiones del tablero: "))

    tablero = crear_tabla(dimensiones)
    print("¡BIENVENIDO A HARTZAI JOKUA - EDICIÓN TUPANDITTA!")
    mostrar_tabla(tablero)

    print() #Visual
    print() #Visual

    while terminado == False: #Termina cuando uno de los jugadores gana (conecta 4 fichas suyas)
        ##  Variables
        valido1 = False #Comienzo asumiendo que el movimiento no es válido
        valido2 = False #Comienzo asumiendo que el movimiento no es válido

        ##  Jugador 1
        while valido1 == False: #El bucle termina cuando el Jugador introduce un movimiento válido
            jugador_1 = int(input('Jugador 1, introduce una columna: '))
            valido1 = movimiento_valido(jugador_1, tablero) #Compruebo si el movimiento es válido

            if valido1 == False:
                print("Columna no válida o llena.")

        tablero = colocar_ficha(jugador_1, '1', tablero) #Introduzco la nuevo ficha
        mostrar_tabla(tablero) #Muestro el tablero con la nuevo ficha

        if comprobar_tabla(tablero, '1') == True: #Compruebo si hay 4 fichas del Jugador 1 conectadas
            print() #Visual
            print() #Visual

            print('¡ENHORABUENA!')
            print('Jugador 1 HAS GANADO')

            break #Se sale del bucle principal (El juego ha terminado)
        
        if tabla_llena(tablero) == True: #Si anteriormente compruebo que el Jugador no tiene 4 fichas conectadas, compruebo si existen huecos libres para nuevas fichas
            print() #Visual
            print() #Visual

            print('¡EMPATE!')
            
            break #Se sale del bucle principal (El juego ha terminado)
        
        print() #Visual
        print() #Visual

        ##  Jugador 2
        while valido2 == False: #El bucle termina cuando el Jugador introduce un movimiento válido
            jugador_2 = int(input('Jugador 2, introduce una columna: '))
            valido2 = movimiento_valido(jugador_2, tablero) #Compruebo si el movimiento es válido

            if valido2 == False:
                print("Columna no válida o llena.")

        tablero = colocar_ficha(jugador_2, '2', tablero) #Introduzco la nuevo ficha
        mostrar_tabla(tablero) #Muestro el tablero con la nuevo ficha

        if comprobar_tabla(tablero, '2') == True: #Compruebo si hay 4 fichas del Jugador 1 conectadas
            print() #Visual
            print() #Visual

            print('¡ENHORABUENA!')
            print('Jugador 2 HAS GANADO')

            break #Se sale del bucle principal (El juego ha terminado)
        
        if tabla_llena(tablero) == True: #Si anteriormente compruebo que el Jugador no tiene 4 fichas conectadas, compruebo si existen huecos libres para nuevas fichas
            print() #Visual
            print() #Visual

            print('¡EMPATE!')
            
            break #Se sale del bucle principal (El juego ha terminado)
        
        print() #Visual
    
    print() #visual


################################            JUGAR
HartzaiJokua() 

