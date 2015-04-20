Este directorio almacena los archivos necesarios para correr el raspberry pi como el robot coordinador del enjambre
los archivos Adafruit son las librerías necesarias para el módulo acelerómetro + magnetómetro.
El archivo testcam.py es un programa de prueba para la raspicam
el archivo gateway.py define la interfaz rf con los robots y hace un HTTP request al servidor para mandar los datos
el archivo cam1.py contiene el programa final con la medición de la distancia con el laser y el envio de los datos
