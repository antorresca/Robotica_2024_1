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

La función `getkey()` (obtenida en este enlace: [http://python4fun.blogspot.com/2008/06/get-key-press-in-python.html](http://python4fun.blogspot.com/2008/06/get-key-press-in-python.html)), se utiliza para capturar la tecla presionada por el usuario.

```
def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c
```

Dependiendo de la tecla que se presione, se realizará un procedimiento diferente:

* Se debe mover hacia adelante y hacia atrás con las teclas W y S
* Debe girar en sentido horario y antihorario con las teclas D y A
* Debe retornar a su posición y orientación centrales con la tecla R
* Debe dar un giro de 180° con la tecla ESPACIO

Las funciones `pubVel()` y `teleport()` se declaran como funciones de ayuda para enviar los mensajes al tópico de velocidad y para llamar a los servicios necesarios para teletransportar la tortuga.

```

def get_action(): 
    key = getkey()
    if key == b'w' or key == b'W':
        pubVel(1,0)
    elif key == b's' or key == b'S':  
        pubVel(-1,0)
    elif key == b'd' or key == b'D':
        pubVel(0,-1)
    elif key == b'a' or key == 'A':
        pubVel(0,1)
    elif key == b'r' or key == 'R':
        teleport('abs')
    elif key == b' ':
        teleport('rel')
```

Definimos la función `pubVel()` con dos parámetros: `linear` y `angular`, valores que corresponden a la velocidad que asignaremos a la tortuga.

En esta primera línea, indicamos que nuestro nodo va a publicar al tópico `/turtle1/cmd_vel` usando un tipo de mensaje  *Twist* .

```
def pubVel(linear, angular):
    pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
```

Luego, declaramos el mensaje como un mensaje de tipo *Twist* y le asignamos los valores correspondientes a la velocidad lineal y la velocidad angular. Por último, publicamos el mensaje.

```
    message = Twist()
    message.linear.x = linear
    message.angular.z = angular
    pub.publish(message)
```

En la función `teleport()`, llamaremos a los servicios correspondientes para lograr que la tortuga regresa a su lugar de inicio o que gire 180°.

En el primer caso, llamamos al servicio `/turtle1/teleport_absolute`, con el cual podemos mover la tortuga a un lugar indicado por tres parámetros: `x`, `y` y `theta`. Estos valores son los mismos que se obtienen al iniciar el nodo de turtlesim.

Además, también se llama al servicio `clear`, con el cual se limpia el fondo de la ventana del turtlesim.

```
def teleport(key):
    if key == 'abs':
        rospy.wait_for_service(teleport_ab)
        try:
            teleport_absolute = rospy.ServiceProxy(teleport_ab, TeleportAbsolute)
            teleport_abs_result = teleport_absolute(5.544445,5.544445,0)

            rospy.wait_for_service('/clear')
            clearTrajec = rospy.ServiceProxy('/clear', Empty)
            Reset = clearTrajec()
        except rospy.ServiceException as e:
            print(str(e))
```

En el segundo caso, se llama al servicio `/turtle1/teleport_relative`, el cual mueve la tortuga una distancia lineal y angular determinadas con respecto a la posición actual de la torguga. Como queremos que gire 180°, la distancia lineal es 0 y la angular es pi.

```
    elif key == 'rel':
        rospy.wait_for_service(teleport_rel)
        try:
            teleport_relative = rospy.ServiceProxy(teleport_rel, TeleportRelative)
            teleport__relative_result = teleport_relative(0,pi)
        except rospy.ServiceException as e:
            print(str(e))
```

En el programa principal damos un mensaje de entrada, donde se indica cuales teclas se utilizan para mover la tortuga.

```
if __name__ == '__main__':
  
    welcome = """
    Made by: Andres Camilo Torres Cajamarca, Brian Enrique Muñoz Garcia
    --------------------------------------------------------------
    Reading from keyboard
    --------------------------------------------------------------
    Use AWSD to move the turtle
    Use 'R' to clear canvas and teleport the turtle to starting position
    Use Space Bar to rotate the turtle 180°
    Use 'q' to quit
    --------------------------------------------------------------
    """
```

Por último, inicializamos un nodo al que nombramos `my_teleop_key`, utilizamos la función `rospy.loginfo()` para mostrar el mensaje, y declaramos un ciclo en el que mientras que no se cierre ROS (con `q` o `CTRL+C`), llamamos a la función `get_action()`, la cual moverá a la tortuga según la tecla correspondiente.

```
    try:
            rospy.init_node('my_teleop_key')
            rospy.loginfo(welcome)
            rate = rospy.Rate(10) # 10hz
            while not rospy.is_shutdown():
                get_action()
                rate.sleep()

    except rospy.ROSInterruptException:
            pass
```


## Resultados

Para el desarrollo de la práctica, primero se realizó el código y se probó en el simulador EPSON RC+ 7.0




El link donde se encuentra el video de la simulación es el siguiente:

## Conclusiones
