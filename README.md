#### Hartzai Jokua - Lógica y Estructura

La base de este proyecto es el tradicional juego del **Conecta 4**, el cual en euskera se dice **Hartzai Jokua**. 
Este juego consiste en lograr `conectar 4` fichas iguales seguidas, ya sea en horizontal, vertical o diagonal.

### Arquitectura del Juego

Este programa está dividido en varias funciones, las cuales se integran finalmente en una misma función (Función General).
Estas funciones tienen como fin...

    --> Iniciar el juego; creando el tablero.
    --> Recopilar los movimientos de los jugadores, y comprobar que son válidos.
    --> Analizar el tablero para determinar el final del juego; cuando alguien **gana**, o en caso de **empate**.

## Flujo del Código

1. Inicio: El programa solicita al usuario las dimensiones del tablero (N).
   --> Validación: Si N < 4, vuelve a pedir el número.
   --> Creación: Genera una matriz de NxN rellena de asteriscos ('*') y la muestra por pantalla.

2. Bucle de Partida (Juego): Se inicia el ciclo principal "while" que se repite hasta que 'terminado' sea True.

    //// Turno Jugador 1 (Ficha 'X'):

        --> Entrada y Validación: Bucle que solicita una columna al usuario.
              % % Si la columna es inválida (fuera de rango o llena): Muestra error y repite la pregunta.
              % % Si es válida: Sale del bucle de validación.

        --> Colocación (Gravedad): La función 'colocar_ficha' busca la fila libre más baja en esa columna y coloca la 'X'.

        --> Visualización: Se muestra el estado actualizado del tablero.

        --> Verificación de Victoria: La función 'comprobar_tabla' revisa filas, columnas y diagonales.
              % % Si hay 4 en línea: Muestra "Jugador 1 has ganado", marca 'terminado' y rompe el bucle (FIN).
              % % Si no: El juego continúa.

        --> Verificación de Empate: La función 'tabla_llena' revisa si quedan huecos ('*').
              % % Si no quedan huecos: Muestra "EMPATE" y rompe el bucle (FIN).

    //// Turno Jugador 2 (Ficha 'O'): (Solo si el juego no terminó en el turno anterior)

        --> Entrada y Validación: Bucle que solicita una columna al usuario.
              % % Si la columna es inválida: Muestra error y repite la pregunta.
              % % Si es válida: Sale del bucle de validación.

        --> Colocación (Gravedad): La función 'colocar_ficha' busca la fila libre más baja en esa columna y coloca la 'O'.

        --> Visualización: Se muestra el estado actualizado del tablero.

        --> Verificación de Victoria: La función 'comprobar_tabla' revisa filas, columnas y diagonales.
              % % Si hay 4 en línea: Muestra "Jugador 2 has ganado", marca 'terminado' y rompe el bucle (FIN).
              % % Si no: El juego continúa.

        --> Verificación de Empate: Se comprueba nuevamente si la tabla está llena.
              % % Si no quedan huecos: Muestra "EMPATE" y rompe el bucle (FIN).

    //// Siguiente Ronda: Si nadie ganó ni hubo empate, el bucle vuelve al inicio para el Turno del Jugador 1.
   
## Optimización del Código

Actualmente el arcvhivo "JUEGO_HartzaiJokua_Base.py" contiene la base del juego. No obstante, existen diferentes mejoras aplicables para mejorar el diseño del programa. 
(las dejo como puntos de mejora para versiones posteriores)

