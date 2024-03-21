# Laboratorio 1 - Robótica Industrial - "Trayectorias, Entradas y Salidas Digitales"

***Participantes***

* Andres Camilo Torres Cajamarca
* Brian Enrique Muñoz Garcia

## Descripción Solución Planteada

Se realizó el proceso de configuración e inserción del controlador y el manipulador IRB 140 a la plataforma RobotStudio, para posteriormente realizar la creación de un sistema de coordenadas en la punta del marcador, que esta anclado a la herranmienta en el diseño CAD , lugo se realizó la creación, ubicación y alineación de la herramienta con la posición de el portaherramienta del manipulador.

Para generar las trayectorias necesarias para dibujar las iniciales, el logo y su nombre, primero se realizó un modelo de estos en Fusion 360. Posteriormente, se incluyó este modelo en la simulación de RobotStudio. Se utilizó un extremo del tablero que contenia el logo y letras como Work Object. De esta manera, se generaron varias trayectorias.

Para generar las trayectorias, se generaron cada uno de los puntos correspondientes a las esquinas de cada letra u objeto en orden de derecha a izquierda. Una vez generados, estos puntos se agregaron a su trayectoria correspondiente, y usando el tipo de movimiento linear (MoveL) con una velocidad de v50 mm/s y un zone de z5 mm. Con esto, en el procedimiento principal, se tenían varias instrucciones.

Durante el desarrollo de la práctica se pudo evidenciar que en ciertos casos al generar los diversos puntos y al habilitar la opción en robot studio de asignar la orientación de cada articulación automaticamente, el robot hacia giros abruptos lo que generaba que llegara a singularidades durante las trayectorias; para solucionar esto, se realizaron cambios en los cuadrantes de las articulación teniendo en cuenta que el robot llegara a las posiciones deseadas.

## Diagrama de Flujo de acciones del robot

![1711047013858](image/README/1711047013858.png)

## Plano de planta de la ubicación de cada uno de los elementos

Para el desarrollo de la práctica se colocó el plano de trabajo a 170 mm desde el suelo (distancia en el eje z) y a 650 mm desde el eje z del robot (distancia en el eje x)

![1710647252012](image/README/1710647252012.png)

![1710818937923](image/README/1710818937923.png)

## Descripción de las funciones empleadas

1. **SetDO** : Esta instrucción se utiliza para **establecer el estado de una salida digital (DO)** en el robot. Por ejemplo, puedes usar `SetDO` para activar o desactivar una señal de salida que controle un dispositivo externo, como una válvula o una luz.
2. **MoveL** : La instrucción `MoveL` se emplea para  **mover el robot en una trayectoria lineal (L)** . Es útil cuando necesitas que el robot siga una línea recta entre dos puntos. Los ejes del robot se mueven simultáneamente hacia el destino, manteniendo la orientación de la herramienta.
3. **MoveJ** : Por otro lado, `MoveJ` permite  **mover el robot de un punto a otro sin seguir necesariamente una línea recta** . En este caso, los ejes del robot alcanzan el punto de destino al mismo tiempo, pero no necesariamente mantienen la orientación de la herramienta.

## Diseño de la herramienta

Para el diseño de la herramienta se consideraron los siguientes parametros de diseño:

* Tamaño del marcador
* Tamaño de soporte principal
* Fuerzas ejercidadas por el robot
* Ángulo de la superficie
* Tolerancias
* Otros

Teniendo en cuenta esto, se tomaron las respectivas medidas del marcador y teniendo en cuenta la hoja de datos del robot se procedió a hacer un boceto de la herramienta como se ve en la siguiente imagen y por facilidad para alcanzar la superficie y evitar tener inconvenientes con la concordancia de los sistemas coordenados se diseñó la herramienta a 45°

![1710210839228](image/README/1710210839228.png)

Una vez teniendo esto, se tuvo en cuenta que la herramienta se pretendía hacer por medio de manufactura aditiva con impresión 3D por lo cual se tenia que tener en cuenta ciertas tolerancias debido a la expansión y contracción termica que podria sufrir el PLA por este método de manufactura.

![1710207357054](image/README/1710207357054.png)

Una vez teniendo en cuenta estos parametros se diseñó la herramienta que se ve en los siguientes planos.

![1710209020377](image/README/1710209020377.png)

![1710209032748](image/README/1710209032748.png)

Al realizar la impresión 3D se obtuvo la siguiente herramienta.

![1710819285335](image/README/1710819285335.png)

## Video Demostrativo

El link donde se encuentra el video de la simulación es el siguiente:

[https://drive.google.com/file/d/1-fkUrs10K-_VG1Xfjn2DbphrHv41BWaV/view?usp=sharing]([https://drive.google.com/file/d/1-fkUrs10K-_VG1Xfjn2DbphrHv41BWaV/view?usp=sharing]())

El link donde se encuentra el video demostrativo del funcionamiento es el siguiente:

[https://drive.google.com/file/d/1xLDvLqA7we9p7A_fknllIuA77fwrY0Xp/view?usp=drive_link]([https://drive.google.com/file/d/1-fkUrs10K-_VG1Xfjn2DbphrHv41BWaV/view?usp=sharing]())
