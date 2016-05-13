from socket import *
import sys
import select
from packet import *  #importa la clase que cree


UDP_IP  = "12.12.12.12"  #direccion del servidor
UDP_PORT = 6005  #puerto que estaremos utilizando
address = (UDP_IP, UDP_PORT)  #se crea un objeto que tiene como atributos direccion y puerto

client_socket = socket(AF_INET, SOCK_DGRAM)   #se crea el objeto del socket

prueba = Packet('req',3,'vote')  ##se crea el objeto del paquete que estaremos enviando
prueba.printing()  #este metodos solo imprime

binary = prueba.toBin()  #se hace el encoding a binario Se agrega delimiter automaticamente porque es string




client_socket.sendto(binary, address)   #sendto manda la informacion a la addres que se abrio
recv_data, addr = client_socket.recvfrom(2048)  #recibe datos y guarda tambien la direccion de donde proviene
DataArray = ''.join(chr(int(recv_data[i:i+8], 2)) for i in xrange(0, len(recv_data), 8)) #convierte de binario a alfanumerico

print "received data: ", DataArray   # imprime la informacion recibida decodificada