% Iniciar el nodo de ROS en MATLAB
rosinit;

% Definir el nombre del tópico y el tipo de mensaje
topic_name = '/turtle1/pose';
message_type = 'turtlesim/Pose';

% Crear el suscriptor
pose_subscriber = rossubscriber(topic_name, message_type);

% Esperar para asegurarse de que se reciba al menos un mensaje
pause(1);

% Capturar el último mensaje recibido
latest_message = receive(pose_subscriber, 1);

% Mostrar la información de la última pose recibida
disp('Última pose recibida:');
disp(latest_message);

% Finalizar el nodo de ROS en MATLAB
rosshutdown;
