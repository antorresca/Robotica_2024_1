import tkinter as tk
from tkinter import PhotoImage
import rospy
import time
from sensor_msgs.msg import JointState
from dynamixel_workbench_msgs.srv import DynamixelCommand

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Laboratorio de robótica No. 4")

# Variables globales para almacenar las posiciones actuales de los motores
current_positions = [0, 0, 0, 0]

# **Frame 1: Título y subtítulos**
frame_titulo = tk.Frame(ventana)
frame_titulo.pack()

# Definir el título principal
titulo = tk.Label(frame_titulo, text="Laboratorio de robótica No. 4  Cinemática Directa- Phantom X- ROS", font=("Arial", 24, "bold"))
titulo.pack(pady=20)

# Definir el subtítulo
subtitulo = tk.Label(frame_titulo, text="Integrantes: Andres Torres y Brian Muñoz", font=("Arial", 12, "bold"))
subtitulo.pack(pady=5)

# **Frame 2: Botones**
frame_botones = tk.Frame(ventana)
frame_botones.pack(side=tk.LEFT, padx=20, pady=20)

def jointCommand(command, id_num, addr_name, value, time):
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command, id_num, addr_name, value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(str(exc))

def mandar_datos(lista):
    global angulos_re
    for i in range(1, 5):
        jointCommand('', i, 'Goal_Position', lista[i-1], 0.5)
        time.sleep(1)
        angulo = round(lista[i-1] / conv)
        print('Angulo Relativo: ' + str(angulo - angulos_re[i-1]))

def callback(data):
    global current_positions
    current_positions = data.position[:4]
    print("Current positions: ", current_positions)
    actualizar_valores_articulaciones()

def listener():
    rospy.Subscriber('/dynamixel_workbench/joint_states', JointState, callback)
    rospy.spin()

def iniciar_nodo_ros():
    rospy.init_node('joint_node', anonymous=False)
    listener_thread = threading.Thread(target=listener)
    listener_thread.start()

global angulos_re
Home = [2017, 2070, 3065, 2069]
conv = 11.376641207027
angulos_re = [round(Home[i] / conv) for i in range(len(Home))]

# Funciones para cada botón
def accion_home():
    imagen_label.config(image=imagen)
    mandar_datos(Home)
    actualizar_valores_articulaciones()

Pose1 = '25,25,20,-20'
valores_conv = Pose1.split(',')
valores_conv = [int(valores_conv[i]) for i in range(len(valores_conv))]
Pose1real = [round(Home[i] + valores_conv[i] * conv) for i in range(len(valores_conv))]

def accion_pose1():
    imagen_label.config(image=imagen1)
    mandar_datos(Pose1real)
    actualizar_valores_articulaciones()

Pose2 = '-35,35,-30,30'
valores_conv = Pose2.split(',')
valores_conv = [int(valores_conv[i]) for i in range(len(valores_conv))]
Pose2real = [round(Home[i] + valores_conv[i] * conv) for i in range(len(valores_conv))]

def accion_pose2():
    imagen_label.config(image=imagen2)
    mandar_datos(Pose2real)
    actualizar_valores_articulaciones()

Pose3 = '85,-20,30,25'
valores_conv = Pose3.split(',')
valores_conv = [int(valores_conv[i]) for i in range(len(valores_conv))]
Pose3real = [round(Home[i] + valores_conv[i] * conv) for i in range(len(valores_conv))]

def accion_pose3():
    imagen_label.config(image=imagen3)
    mandar_datos(Pose3real)
    actualizar_valores_articulaciones()

Pose4 = '80,-35,30,-45'
valores_conv = Pose4.split(',')
valores_conv = [int(valores_conv[i]) for i in range(len(valores_conv))]
Pose4real = [round(Home[i] + valores_conv[i] * conv) for i in range(len(valores_conv))]

def accion_pose4():
    imagen_label.config(image=imagen4)
    mandar_datos(Pose4real)
    actualizar_valores_articulaciones()

# Crear y colocar los botones
boton_home = tk.Button(frame_botones, text="Home", command=accion_home, width=14, height=6)
boton_home.pack(pady=5)

boton_pose1 = tk.Button(frame_botones, text="Pose 1", command=accion_pose1, width=14, height=6)
boton_pose1.pack(pady=5)

boton_pose2 = tk.Button(frame_botones, text="Pose 2", command=accion_pose2, width=14, height=6)
boton_pose2.pack(pady=5)

boton_pose3 = tk.Button(frame_botones, text="Pose 3", command=accion_pose3, width=14, height=6)
boton_pose3.pack(pady=5)

boton_pose4 = tk.Button(frame_botones, text="Pose 4", command=accion_pose4, width=14, height=6)
boton_pose4.pack(pady=5)

# **Frame 3: Valores articulares**
frame_valores = tk.Frame(ventana)
frame_valores.pack(side=tk.LEFT, padx=20, pady=20)

# Etiquetas para valores de articulaciones
valor_joint1 = tk.StringVar(value="0")
valor_joint2 = tk.StringVar(value="0")
valor_joint3 = tk.StringVar(value="0")
valor_joint4 = tk.StringVar(value="0")

etiqueta_joint1 = tk.Label(frame_valores, text="JOINT1: " + valor_joint1.get(), font=("Arial", 20))
etiqueta_joint1.pack(pady=5)

etiqueta_joint2 = tk.Label(frame_valores, text="JOINT2: " + valor_joint2.get(), font=("Arial", 20))
etiqueta_joint2.pack(pady=5)

etiqueta_joint3 = tk.Label(frame_valores, text="JOINT3: " + valor_joint3.get(), font=("Arial", 20))
etiqueta_joint3.pack(pady=5)

etiqueta_joint4 = tk.Label(frame_valores, text="JOINT4: " + valor_joint4.get(), font=("Arial", 20))
etiqueta_joint4.pack(pady=5)

# **Frame 4: Imagen**
frame_imagen = tk.Frame(ventana)
frame_imagen.pack(side=tk.RIGHT, padx=20, pady=20)

imagen = PhotoImage(file="Images/HOME.png")
imagen1 = PhotoImage(file="Images/Pose1.png")
imagen2 = PhotoImage(file="Images/Pose2.png")
imagen3 = PhotoImage(file="Images/Pose3.png")
imagen4 = PhotoImage(file="Images/Pose4.png")

imagen_label = tk.Label(frame_imagen, image=imagen)
imagen_label.pack()

# Función para actualizar valores de articulaciones
def actualizar_valores_articulaciones():
    global current_positions
    valor_joint1.set(str(current_positions[0]))
    valor_joint2.set(str(current_positions[1]))
    valor_joint3.set(str(current_positions[2]))
    valor_joint4.set(str(current_positions[3]))

    etiqueta_joint1.config(text="JOINT1: " + valor_joint1.get())
    etiqueta_joint2.config(text="JOINT2: " + valor_joint2.get())
    etiqueta_joint3.config(text="JOINT3: " + valor_joint3.get())
    etiqueta_joint4.config(text="JOINT4: " + valor_joint4.get())

# Iniciar el nodo ROS en un hilo separado
import threading
threading.Thread(target=iniciar_nodo_ros).start()

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
