# deteccion de colores
#

import io 
import cv2
import numpy as np
import picamera
import picamera.array
import time
import math


def distancia(y):
    h= 2.1
    K = 10.0
    offset = 2.3
    theta = K*abs(300-y)+offset
    tanTheta = math.tan(theta)
    dist = 1 / tanTheta
    return dist 

camara = picamera.PiCamera()
camara.resolution = (160, 600)


while(1):
    stream = picamera.array.PiRGBArray(camara)
    camara.capture(stream, format='bgr')
    img = stream.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binario = cv2.threshold(gray,200, 255, cv2.THRESH_BINARY)
    momentos = cv2.moments(binario)
    area = momentos['m00']
 
    if(area > 20):
         
        #Buscamos el centro x, y del objeto
        x = int(momentos['m10']/momentos['m00'])
        y = int(momentos['m01']/momentos['m00'])
         
        #Mostramos sus coordenadas por pantalla
        #print "x = ", x
        #print "y = ", y
	      print "distancia: "+str(distancia(y)) + "cm"
	      
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
    
cv2.destroyAllWindows()

