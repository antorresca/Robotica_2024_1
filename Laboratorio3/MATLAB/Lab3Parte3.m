% Iniciar ROS en MATLAB
rosinit;

% Crear un cliente de servicio para el servicio teleport_absolute
teleportClient = rossvcclient('/turtle1/teleport_absolute');

% Crear una solicitud de servicio
teleportRequest = rosmessage(teleportClient);

% Definir las coordenadas de la posición deseada
teleportRequest.X = 3.0; % Posición en el eje x
teleportRequest.Y = 3.0; % Posición en el eje y
teleportRequest.Theta = pi; % Ángulo de orientación

% Llamar al servicio teleport_absolute
teleportResponse = call(teleportClient, teleportRequest);

% Cerrar ROS en MATLAB
rosshutdown;

