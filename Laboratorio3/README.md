# Laboratorio 3 - Robótica de Desarrollo, Intro a ROS

***Participantes***
__Andres Camilo Torres Cajamarca__
__Brian Enrique Muñoz Garcia__

## Metodología

### Matlab:

### Python:

Para esta sección del laboratorio fue necesario crear un script dentro del paquete *hello_turtle* el cual permitiera operar una tortuga del paquete *turtlesim* con el teclado. El script realizado tiene por nombre [myTeleopKey.py](https://github.com/vahernandezmo/robotica_lab/blob/master/Laboratorio_3/python/myTeleopKey.py)

Primero se importan las librerías necesarias para correr los nodos de ROS y para capturar las teclas presionadas.

```
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
from std_srvs.srv import Empty
import termios, sys, os
from numpy import pi
```

Posteriormente, delcaramos como constantes tanto el topic para publicar la velocidad, como los servicios para poder ubicar la tortuga en el centro o girarla 180°.

```
cmd_vel_topic = '/turtle1/cmd_vel'
teleport_ab = '/turtle1/teleport_absolute'
teleport_rel = '/turtle1/teleport_relative'
```




## Resultados

Para el desarrollo de la práctica, primero se realizó el código y se probó en el simulador EPSON RC+ 7.0




El link donde se encuentra el video de la simulación es el siguiente:

## Conclusiones
