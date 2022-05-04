import cv2 as ocv
import mediapipe as mp
import numpy as np
import math
import serial
import time



ard = serial.Serial('COM7',9600)
time.sleep(2)

 
conar = 0
camara = ocv.VideoCapture(0)
contador = 0
manitas = mp.solutions.hands
dibuja = mp.solutions.drawing_utils
pintar = (0,0,250)
guardado = ocv.VideoWriter("asdasd.avi", ocv.VideoWriter_fourcc(*'XVID'), 20.0, (640,480))

with manitas.Hands(
    static_image_mode = False,
    max_num_hands = 1,
    model_complexity = 0,
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.9
    ) as hands:

   
    while True:
        so,img = camara.read()
        hig, width ,_ = img.shape

        img_flags_writeable = False
        img = ocv.cvtColor(img, ocv.COLOR_BGR2RGB)
        resultado = hands.process(img)
        img = ocv.cvtColor(img, ocv.COLOR_RGB2BGR)
        img_flags_writeable = True
        #aux = img.copy()
        if resultado.multi_hand_landmarks:
            for lmarks in resultado.multi_hand_landmarks:


                #para dibujar lineas en toda la mano
                """dibuja.draw_landmarks(
                    aux,
                    lmarks,
                    manitas.HAND_CONNECTIONS,
                    dibuja.DrawingSpec(color = (0,0,250), thickness = 2, circle_radius = 2),
                    dibuja.DrawingSpec(color = (0,250,0), thickness = 3)
                )"""


                """
                x = int (lmarks.landmarks[4].x * w)
                y = int (lmarks.landmarks[4].y * h)
                ocv.circle(img, (x,y), 10, pintar, 3)
                ocv.circle(img, (x,y), 5, pintar, 3)
                print(resultado.multi_hand_landmarks)"""

                #putno especifico
                #punta tres dedos

                #anular
                xm = lmarks.landmark[manitas.HandLandmark.MIDDLE_FINGER_TIP].x * width
                ym = lmarks.landmark[manitas.HandLandmark.MIDDLE_FINGER_TIP].y * hig


                #medio
                xa = lmarks.landmark[manitas.HandLandmark.RING_FINGER_TIP].x * width
                ya = lmarks.landmark[manitas.HandLandmark.RING_FINGER_TIP].y * hig


                #indice
                xi = lmarks.landmark[manitas.HandLandmark.INDEX_FINGER_TIP].x * width
                yi = lmarks.landmark[manitas.HandLandmark.INDEX_FINGER_TIP].y * hig

                #punta pulgar
                x1 = lmarks.landmark[manitas.HandLandmark.THUMB_TIP].x * width
                y1 = lmarks.landmark[manitas.HandLandmark.THUMB_TIP].y * hig

                #longitud de la linea entre los puntos

                indice = math.hypot(x1 - xi, y1 - yi)
                medio = math.hypot(x1 - xm, y1 - ym)
                anular = math.hypot(x1 - xa, y1 - ya)

                #Combertir a enteros para poder transformarlos y pasarlos a arduino            
                xm = (int(xm))
                ym = (int(ym))
                xa = (int(xa))
                ya = (int(ya))
                xi = (int(xi))
                yi = (int(yi))
                x1 = (int(x1))
                y1 = (int(y1))



                indice = int(indice)
                medio = int(medio)
                anular = int(anular)

                #dibuja los circulos y las lineas de los tres dedos seleccionados

                ocv.circle(img, (x1,y1), 3,  (250,250,250), 2)
                ocv.circle(img, (xm,ym), 3,  (250,250,250), 2)
                ocv.circle(img, (xa,ya), 3,  (250,250,250), 2)
                ocv.circle(img, (xi,yi), 3,  (250,250,250), 2)
                ocv.line(img, (x1, y1), (xm, ym), (0,0,0), 3)
                ocv.line(img, (x1, y1), (xa, ya), (0,0,0), 3)
                ocv.line(img, (x1, y1), (xi,yi), (0,0,0), 3)


                #descomentar para diversion quita los """codigo codigo codigo"""
                """if lime > 200:
                    #ocv.putText(img, "puto el que lo lea", (20, 360), ocv.FONT_HERSHEY_SIMPLEX , 2, (250,0,0), 3)
                    ard.write(b'q')
                if lime < 50:
                    ard.write(b'a')"""

                #lo multiplico por 1.388888888 y lo divido entre uno y medio para pasar
                #el limite de rotacion de los servomotores

                indice = (indice * 1.3888) /1.2
                medio = (medio * 1.3888) /1.2
                anular = (anular * 1.3888) /1.2

                indice = int(indice)
                medio = int(medio)
                anular = int(medio)

                #indice = str(indice)
                #medio = str(medio)
                #anular = str(anular)

                
                #a = ard.write(bin(indice))
                #b = ard.write(bin(medio))
                #c = ard.write(bin(anular))
                #indice = bin(indice)
                #medio = bin(medio)
                #anular = bin(anular)


                #pasamos los valores de los tres dedos a un array para enviarlos al mismo tiempo por el puerto serial
                
                info = []
                info = [indice, medio, anular]


                #lo envia por puerto serie a arduino
                ard.write(info)

                #print(info)

        #ocv.imshow("asd", aux)
        ocv.imshow("img", img)
        if ocv.waitKey(1) & 0xFF == ord('q'):
            break
                   
camara.release()
ocv.destroyAllWindows()



