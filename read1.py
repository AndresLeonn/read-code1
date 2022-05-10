import cv2
import numpy as np
#libreria numpy especializada en el calculo numerico y analisis de datos 
bgr=np.zeros((300,300,3),dtype=np.uint8)#bgr es una lista - np.zeros es para devolver un array en ceros
bgr[:,:,:]=(0,255,255)#np.uint8 toma valores absolutos y toma una matriz de 0 a 255 y se define los valores de rgb
cv2.imshow('BGR',bgr)#cv2.imshow es para mostrar una imagen en una ventana y la ventana se ajusta automaticamente al tamaño de la imagen 


cv2.waitKey(0)#espera una tecla para cointinuar con la siguiente instruccion dentro del parentesis el tiempo en milisegundos que debe esperar luego de oprimir la tecla 
cv2.destroyAllWindows()#para cerrar la ventana apenas se oprima la tecla 
