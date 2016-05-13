  #!/usr/bin/env python
    
import socket
import binascii
from RX import *
   
candidates = [0,0,0,0,0]
TCP_IP = '12.12.12.12'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)
  

while 1:
      conn, addr = s.accept()   #acepta la conexion 
      print 'Connection address:', addr
      data = ""
      
      data = conn.recv(BUFFER_SIZE)  #recibe datos
     
     
      if not data: break
      print "received data:", data
      DataArray = ''.join(chr(int(data[i:i+8], 2)) for i in xrange(0, len(data), 8))  #convierte de binario a lfanumerico
      
      packet = Packet(DataArray)  #lo hace tipo Packet
      packet.printing()
     


      ToRes =  packet.desicion(candidates) #toma la decision en base a si es vote o query
     
      ToRes.printing()
      binary = ToRes.toBin()   #convierte respuesta a binario se agrega delimiter automaticamente porque es un string

      
      print binary
      i = 0;
      length=len(binary)
      print length
      conn.send(binary) #manda el paquete binario string armado 
  

conn.close()
