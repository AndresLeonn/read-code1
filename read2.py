import cv2
from cv2 import imshow 
# cv2 biblioteca de enlaces de Python diseñada para resolver problemas de visión artificial
"""import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'"""

imgText="cafe"#define una veriable con una cadena de texto
#Lectura de imagen
img= cv2.imread(imgText+'.png')#imread es un metodo que carga una imagen - devuelve una matriz vacia en caso de que no se pueda leer la imagen por algun error de compatibilidad 
#hace una concatenacion para dar el mnombre de la imagen y lo define en otra variable img 
imshow('Imagen Original',img) #imshow sirve para mostrar una imagen en una ventana primero le da el texto del titulo de la venta luego la imagen a cargar 


cv2.waitKey(0) #espera la tecla y se le da una espera en milisegundos 
cv2.destroyAllWindows()#cierra la ventana luego de presionar la tecla