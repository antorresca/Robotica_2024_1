import rospy
import time
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from dynamixel_workbench_msgs.srv import DynamixelCommand

__author__ = "F Gonzalez, S Realpe, JM Fajardo"
__credits__ = ["Felipe Gonzalez", "Sebastian Realpe", "Jose Manuel Fajardo", "Robotis"]
__email__ = "fegonzalezro@unal.edu.co"
__status__ = "Test"

# Variables globales para almacenar las posiciones actuales de los motores
current_positions = [0, 0, 0, 0]

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
    '''
    Function: Function to take angle values in terms that dynamixel motors can understand and
              send them to the motors through commands, printing the theoretical value they should reach.
              *Disclaimer: DOES NOT READ VALUES FROM THE MOTOR, ONLY DOES A LINEARIZATION TRANSFORMATION*
    Variables:
    lista: List of 4 int elements in the format A, B, C, D where A, B, C, and D are the desired angles considering the Home position of the robot.
    '''
    global angulos_re  # Global variable storing theoretical angle values from HOME position
    for i in range(1, 5):
        '''
        For loop that iterates over each motor and sends the value in motor scale of the desired angle
        '''
        jointCommand('', i, 'Goal_Position', lista[i-1], 0.5)
        time.sleep(1)
        angulo = round(lista[i-1] / conv)  # Conversion from motor value to angle
        print('Angulo Relativo: ' + str(angulo - angulos_re[i-1]))  # Offset because home is not 0 for each motor

def callback(data):
    '''
    Callback function to handle data received from the joint_states topic.
    Updates the global variable current_positions with the latest positions of the motors.
    '''
    global current_positions
    current_positions = data.position[:4]  # Assuming the first 4 positions correspond to the motors we are interested in
    print("Current positions: ", current_positions)

def listener():
    '''
    Function to initialize the ROS node and subscriber.
    '''
    rospy.init_node('joint_node', anonymous=False)
    rospy.Subscriber('/dynamixel_workbench/joint_states', JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        global angulos_re
        Home = [2017, 2070, 3065, 2069]  # Values of HOME found with Dynamixel Wizard
        conv = 11.376641207027  # Conversion factor found by linearization
        angulos_re = [round(Home[i] / conv) for i in range(len(Home))]
        
        # Start the subscriber in a separate thread
        import threading
        listener_thread = threading.Thread(target=listener)
        listener_thread.start()

        mandar_datos(Home)  # Bring the robot to HOME to start routine
        while True:
            valores = input('Ingrese valores de angulos (Formato: A,B,C,D)')  # Request user for desired angle values
            valores_conv = valores.split(',')
            valores_conv = [int(valores_conv[i]) for i in range(len(valores_conv))]
            valores_real = [round(Home[i] + valores_conv[i] * conv) for i in range(len(valores_conv))]  # Values in scale that Dynamixel motors can understand
            mandar_datos(valores_real)
    except rospy.ROSInterruptException:
        pass
