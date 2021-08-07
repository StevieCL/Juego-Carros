# Reto-Sofka
Solución al reto técnico de Sofka para aplicar a su Training League. 


## Funcionamiento del programa 

Inicialmente el programa le pedirá al usuario que ingrese por teclado un identificador (string) para el juego, luego
procederá a preguntar si se desea crear un nuevo jugador, aceptando como respuesta 'si' o 'no' y así mismo se creará 
un nuevo objeto Jugador, a la vez que imprime el nombre que tendrá el conductor asociado a tal Jugador. Es importante
aclarar que el juego correrá SOLO si se registran al menos 3 jugadores (los necesarios para que exista un podio de 
tres puestos). Posteriormente, se pedirá al usuario que ingrese la cantidad de kilómetros (km) que desea que tenga 
como longitud la pista a recorrer. Inicia la carrera y empiezan a moverse los carros de los jugadores a medida que 
se les asigna turnos de forma aleatoria y se lanza el dado. Finalmente cuando tres carros crucen la meta, el programa 
muestra en pantalla los conductores que ocuparon los tres puestos del podio. Seguidamente, se le pregunta al jugador 
si quiere correr otra carrera; si la respuesta es 'si', se le pide al jugador que especifique nuevamente la cantidad 
de kilómetros (km) para la longitud de la carrera, pero si la respuesta es 'no', se concluye la etapa de carreras, se 
muestra en pantalla una tabla (DataFrame)  con la lista de los jugadores con sus nombres de conductores y el número de 
veces que ocupó cada puesto en el podio. 
Automáticamente se  genera un archivo csv llamado 'Datos_id.csv' donde id corresponde al identificador que se le dio al 
juego.  El juego termina imprimiendo un mensaje de despedida para el jugador.

## Archivos

* Los archivos **Podio, Carro, Carril, Conductor, Pista y Jugador** contienen las clases correspondientes a su nombre. 
* El archivo **Juego** corresponde a la clase Juego y contiene la mayoría de los métodos que serán utilizados durante
el desarrollo del juego como tal. 
* El archivo **Game** es el que se debe correr para empezar a jugar. 

## Requerimientos

Python 3, Pandas instalado en la máquina y ganas de divertirse.
