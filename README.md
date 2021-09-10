# Game_Hundir_la_flota

El tablero de este juego será una matriz de 10x10 dimensiones, matriz sobre la que palmaremos el estado de cada turno. Cada matriz de información continente del estado en cada momento, se mostrará por pantalla.

### Las reglas son las siguientes:

- Cada jugador deberá colocar en su tablero:
    - 4 barcos tamaño 2x1. 

    - 3 barcos tamaño 3x1.

    - 2 barcos tamaño 4x1.
    
    - 1 barco tamaño 5x1. 
    

- En cada turno, el jugador correspondiente debe elegir una casilla de la matriz (10x10) y ambos jugadores marcarán la casilla en la matriz.
- Si la casilla que se ha elegido es agua, será marcada como un una "**o**" y si la casilla que ha marcado es uno de los barcos, la casilla será marcada con una "**x**". 
- Los barcos han de ser mostrados con un "__#__" en la matriz. 
- Los espacios con agua serán mostrados como " " ó "**~**".

Antes de que comience la partida, cada jugador deberá crear su estado inicial. El estado inicial es una configuración de la matriz con todos los barcos colocados. Para ello, el programa debería preguntar, uno a uno, dónde se quiere colocar cada barco. El estilo de pregunta, ha de ser: 

- Inserte la posición del barco 1 (2x1). El usuario ha de escribir si se quiere insertar en la 4a fila, en horizontal y ocupando las últimas dos columnas: `4h9:10`.
- Inserte la posición del barco 2 (2x1). El usuario ha de escribir si se quiere insertar en la 8a fila, en horizontal y ocupando las dos primeras columnas: `8h1:2`.
- Inserte la posición del barco 3 (5x1). Si se quiere colocar en vertical empezando por la fila 1 a la 5 y columna 8: `8v1:5`.

También tendrás la opción de cargar una partida anteriormente definida en formato Json.

Para saber quién empieza a jugar, los jugadores deberán ponerse de acuerdo para que uno de ellos sea el que llame a una función que devuelva dos valores random del 1 al 6, de tipo entero. El primer valor que se muestre por pantalla será el correspondiente al jugador que llama a la función, el segundo será el del contrincante. Quien saque un valor más alto, empieza. 

Además, el programa guardará el nombre de los jugadores y el histórico, es decir, todos los estados de la partida. Para ello se utilizará el formato JSON.

Cuando un jugador haya creado su estado inicial, este estado también deberá ser guardado en formato JSON. Antes de que se inicie la partida, el otro jugador deberá cargar tu estado inicial y tú el suyo. El estado inicial del enemigo es el que usará tu programa para comprobar si las coordenadas que has utilizado han acertado en el blanco o no. 

El formato de preguntas por turno es: 

- `Inserte coordenadas a atacar:`. La respuesta válida será `0x8` --> fila 0, columna 8. 

Una vez insertada las coordenadas, deberá resultar que aparezcan tu matriz y la matriz de estado de tu enemigo, esta última con la nueva coordenada marcada sin la flota excepto si el torpedo hubiera dado en el blanco. 