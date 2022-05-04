#CONTROL DE SERVOMOTORES CON MOVIMIENTO DE MANOS -- ARDUINO PYTHON#

Parta este proyecto se uso opencv y mediapipe para poder activar y traer informacion de la camara, y despues de eso poder reconocer los movimientos de las manos.

Ademas de eso se uso la libreria serial para establecer la comunicacion con un arduino.

Para instalar las librerias ya mencionadas, y librerias que hagan otros trabajos que mencionaremos mas adelante, copie y pegue las siguientes lineas en su cmd:

pip install pyserial
pip install opencv-python
pip install mediapipe
pip install numpy
pip install python-math
pip install python-time

***************************

Despues de instalar las librerias necesarias debe saber que el codigo escrito no funciona para todas las computadoras, así que tendra que mover algunos valores para que funcione en la suya, asi que me encargare de poner las instrucciones con el mayor detalle y explicarlas de forma que pueda entenderlas.


Lo primero que debe hacer en cualquier caso es tener un arduino de otro modo el puerto serial no podra ser establecido, o si no puede conseguir uno y aun quiere porobar el reconocimiento de manos adelanese a el penultimo parrafo donde explicamos que podria hacer.

Una vez tenga el arduino debe conectarlo y revisar en que puerto esta conectado, en mi caso se conecto automaticamente en el puerto "COM7" si no es su caso deve cambiar el puerto, que usualmente es "COM4".

Ya establecido el pueto debe establecer la velocidad de transmicion de informacion, eso se puede ver en el puerto serial de el interprete de arduino, en la parte inferior derecha, que en mi caso es "9600".

***************************************

Una vez establecida la comunicacion con arduino lo unoco que debe hacer es centrarse en el codigo que he dejado para usted.

***************************************

Si tiene una camara externa conectada a su computador debe saber que es probable que tenga un arror "'NoneType' object has no attribute 'shape'", lo que debe hacer es cambiar el numero "0" en la variable "camara" por un "1", y si no funciona solo vaya aumentando el numero hasta que se logre la coneccion.

Ahora ya sera posible enviar informacion entre python y arduino con la informacion de sus manos, usted debera escribir el codigo de arduino, puede usar la libreria "servo.h" y debera buscar como se reciben arrays por el puerto serial para extraer la informacion.

El sugiente punto que puede tener en cuenta pero no es necesario es dentro del bucle "while True", en la parte comentada por los "  """  " si descomenta toda esa seccion, mas la bariable que se encuentra un par de lineas arriba, "aux = img.copy()" y casi al final descomenta la linea " #ocv.imshow("asd", aux)" mostrara en pantalla una segunda ventana de video que mostrara todas las conecciones entre su mano, escencialmente no tiene funcion pero sera divertido de ver.

Si quiere grabar un video de usted moviendo sus manos con las lineas puede descomentar otra seccion del codigo:

Antes de iniciar el bucle While hay una linea comentada llamada "guardado" solo descomentela, despues vaya dentro del bucle y descomente la variable "#aux = img.copy()", y por ultimo vaya hasta el final del codigo y haga lo mismo con "guardado.write(aux)"y si solo quiere hacerlo con el video de las lineas en sus tres dedos solo tiene qie descomentar la linea "guardado.write(img)".

Si no cuenta con un arduino puede comentar las lineas de codiogo "ard = serial.Serial('COM7',9600)
time.sleep(2)" y la linea "ard.write(info)" asi podra usar el programa sin que salte algun error por no contar con el puerto serie activado

Ahora, para terminar, si quiere poner algo de texto en pantalla y divertirse un poco puede descomentar la linea 118 a 122
