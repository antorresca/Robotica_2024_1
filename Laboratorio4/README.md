<<<<<<< Updated upstream
# Laboratorio 4 - Robótica de Desarrollo, Intro a ROS
=======

# Laboratorio 4 - Cinemática Directa- Phantom X- ROS
>>>>>>> Stashed changes

***Participantes***

* Andres Camilo Torres Cajamarca
* Brian Enrique Muñoz Garcia

## Metodología

<<<<<<< Updated upstream
### Cinemática directa

![1716430255455](image/README/1716430255455.png)

## Resultados

## Conclusiones
=======
### Mediciones:


### Análisis:

Parámetros DH del robot Phantom X Pincher:



## ROS

## HMI

A continuación se presenta el código desarrollado para la interfaz:

```
import tkinter as tk
from tkinter import PhotoImage  # Importar PhotoImage

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Laboratorio de robótica No. 4")


# Definir el título principal
titulo = tk.Label(ventana, text="Laboratorio de robótica No. 4  Cinemática Directa- Phantom X- ROS", font=("Arial", 24, "bold"))
titulo.pack(pady=20)

# Definir el subtítulo
subtitulo = tk.Label(ventana, text="Integrantes: Andrés Torres y Brian Muñoz", font=("Arial", 12, "bold"))
subtitulo.pack(pady=5)


# Marco para los botones
marco_botones = tk.Frame(ventana)
marco_botones.pack(side=tk.LEFT, padx=20, pady=20)

# Funciones para cada botón (aún no implementadas)
def accion_home():
    # Implementar la acción para la pose Home
    pass

def accion_pose1():
    # Implementar la acción para la pose 1
    actualizar_valores_articulaciones()

def accion_pose2():
    # Implementar la acción para la pose 2
    actualizar_valores_articulaciones()

def accion_pose3():
    # Implementar la acción para la pose 3
    actualizar_valores_articulaciones()

def accion_pose4():
    # Implementar la acción para la pose 4
    actualizar_valores_articulaciones()

# Crear y colocar los botones
boton_home = tk.Button(marco_botones, text="Home", command=accion_home)
boton_home.pack(pady=5)

boton_pose1 = tk.Button(marco_botones, text="Pose 1", command=accion_pose1)
boton_pose1.pack(pady=5)

boton_pose2 = tk.Button(marco_botones, text="Pose 2", command=accion_pose2)
boton_pose2.pack(pady=5)

boton_pose3 = tk.Button(marco_botones, text="Pose 3", command=accion_pose3)
boton_pose3.pack(pady=5)

boton_pose4 = tk.Button(marco_botones, text="Pose 4", command=accion_pose4)
boton_pose4.pack(pady=5)


# Etiquetas para valores de articulaciones
valor_joint1 = tk.StringVar(value="0")
valor_joint2 = tk.StringVar(value="0")
valor_joint3 = tk.StringVar(value="0")
valor_joint4 = tk.StringVar(value="0")

etiqueta_joint1 = tk.Label(ventana, text="JOINT1: " + valor_joint1.get(), font=("Arial", 12))
etiqueta_joint1.pack(pady=5)

etiqueta_joint2 = tk.Label(ventana, text="JOINT2: " + valor_joint2.get(), font=("Arial", 12))
etiqueta_joint2.pack(pady=5)

etiqueta_joint3 = tk.Label(ventana, text="JOINT3: " + valor_joint3.get(), font=("Arial", 12))
etiqueta_joint3.pack(pady=5)

etiqueta_joint4 = tk.Label(ventana, text="JOINT4: " + valor_joint4.get(), font=("Arial", 12))
etiqueta_joint4.pack(pady=5)


# Función para actualizar valores de articulaciones
def actualizar_valores_articulaciones():
    # Implementar la lógica para obtener los valores de las articulaciones
    # Actualizar las variables StringVar con los nuevos valores
    valor_joint1.set("Nuevo valor Joint 1")
    valor_joint2.set("Nuevo valor Joint 2")
    valor_joint3.set("Nuevo valor Joint 3")
    valor_joint4.set("Nuevo valor Joint 4")

    # Actualizar las etiquetas con los valores de las variables
    etiqueta_joint1.config(text="JOINT1: " + valor_joint1.get())
    etiqueta_joint2.config(text="JOINT2: " + valor_joint2.get())
    etiqueta_joint3.config(text="JOINT3: " + valor_joint3.get())
    etiqueta_joint4.config(text="JOINT4: " + valor_joint4.get())
# Iniciar el bucle principal de la interfaz
ventana.mainloop() 
```


## Resultados

Vídeo del brazo alcanzando cada posición solicitada.
Vídeo demostración de uso de la interfaz de usuario.
Gráfica digital de las poses comparándola con la fotografía del brazo real en la misma configuración.
>>>>>>> Stashed changes
