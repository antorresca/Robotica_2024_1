"""
Allows to use the service dynamixel_command 
"""
import rospy
import time
from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand

__author__ = "F Gonzalez, S Realpe, JM Fajardo"
__credits__ = ["Felipe Gonzalez", "Sebastian Realpe", "Jose Manuel Fajardo", "Robotis"]
__email__ = "fegonzalezro@unal.edu.co"
__status__ = "Test"

def jointCommand(command, id_num, addr_name, value, time):
    #rospy.init_node('joint_node', anonymous=False)
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:        
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command,id_num,addr_name,value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(str(exc))

def mandar_datos(lista):
    '''
    Function: Funcion para tomar valores de angulos en valores que los motores dynamixel pueda entender y
              los manda a los motores por medio de comandos e imprime a que valor teorico debe llegar 
              *Disclaimer: NO SE LEE LOS VALORES DEL MOTOR, SOLO SE HACE UNA TRANSFORMACION POR LINEALIZACION*
    Variables:
    lista: Lista de 4 elementos de tipo int con formato A,B,C,D donde A,B,C y D son los angulos deseados teniendo en cuenta la posicion de Home del robot
    '''
    global angulos_re #Variable global que guarda los valores en angulos teoricos de la posicion HOME
    for i in range(1,5,1):
        '''
        For que itera en cada uno de los motores y manda el valor en escala del motor del angulo deseado 
        '''
        jointCommand('', i, 'Goal_Position', lista[i-1], 0.5) 
        time.sleep(1)
        angulo = round(lista[i-1]/conv) #Conversion del valor del motor a angulo
        print('Angulo Relativo: '+str(angulo-angulos_re[i-1])) #Desfase porque el home no es el 0 de cada motor

if __name__ == '__main__':
    try:
        global angulos_re
        Home = [2017,2070,3065,2069] #Valores de HOME hallados con Dynamixel Wizard
        conv = 11.376641207027 #Factor de conversion hallado por linealizacion
        angulos_re = [round(Home[i]/conv) for i in range(len(Home))] 
        mandar_datos(Home) #Llevar el robot a HOME para empezar rutina
        while True:
            valores = input('Ingrese valores de angulos (Formato: A,B,C,D)') #Solicita al usuario los valores de los angulos a los que se desea llegar
            valores_conv = valores.split(',')
            valores_conv = [int(valores_conv[i]) for i in range(len(valores_conv))]
            valores_real = [round(Home[i]+valores_conv[i]*conv) for i in range(len(valores_conv))] #Valores en escala que los motores Dynamixel pueda comprender
            mandar_datos(valores_real)
    except rospy.ROSInterruptException:
        pass
