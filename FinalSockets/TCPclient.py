#!/usr/bin/env python
    
import socket
from packet import *
import binascii
    
TCP_IP = '12.12.12.12'
TCP_PORT = 5005
BUFFER_SIZE = 16777216


i=0;

prueba = Packet('req',1,'vote') #se arma paquete a enviar
prueba.printing()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #se crea el socket que se usara
s.connect((TCP_IP, TCP_PORT))   ##intenta hacer la conexion al server



binary = prueba.toBin()  #encoding a binario (str) ahi se agrega el delimiter automaticamente al final de los strings




print binary

#print toSend

s.send(binary)  #enviado de informacion
data = s.recv(BUFFER_SIZE)  #recibe respuesta
s.close()

DataArray = ''.join(chr(int(data[i:i+8], 2)) for i in xrange(0, len(data), 8)) #conversion de binario a alfanumerico
print "received data:", DataArray #impresion de informacion recibida decodificada

