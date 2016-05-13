from socket import *
import sys
import select
from RX import *

UDP_IP  = "12.12.12.12"  #direccion el server
UDP_PORT = 6005 #puerto con el que se trabajara
address = (UDP_IP, UDP_PORT)  
candidates = [0,0,0,0,0]  #inicializacion del arreglo que guardara los votos


server_socket = socket(AF_INET, SOCK_DGRAM)  #se crea  el socket
server_socket.bind(address)  #se forza a usar ese socket para estuchar 

while(1):
    print "Listening"
    recv_data, addr = server_socket.recvfrom(2048)  #recibe los datos del cliente y guarda su direccion para regresar la informacion solicitada
    print recv_data
    DataArray = ''.join(chr(int(recv_data[i:i+8], 2)) for i in xrange(0, len(recv_data), 8))   #convierte de binario a alfanumerico
    packet = Packet(DataArray)  #toma el string que recibe y lo convierte en un dato tipo Packet
    packet.printing()

    ToRes = packet.desicion(candidates)  #desicion es el metodo que checa si es query o vote y hace lo que es necesario
    ToRes.printing()

    binary = ToRes.toBin()  #convierte el string que enviaremos de vuelta a binario (str) se agrega automaticamente el delimiter al final porque es string

    print binary
    



    server_socket.sendto(binary, addr)   #envia binario a la direccion que guardo de donde provenian los datos
    
