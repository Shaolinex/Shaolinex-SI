"""
Created on Wed Sep 29 09:30:01 2021

@author: Andres Ducaud / Marcela Linconao
"""
#%% 
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#%% Se inicia la conexion con el host
print("Cliente") # A veces no sabiamos que consola era que
Host = "LocalHost"
Puerto = 8000


Mi_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Mi_Socket.connect((Host, Puerto))



#%% 

Recibir = Mi_Socket.recv(1024)

with open("llaves/keys.pem","r") as archivo:
    llave = RSA.importKey(archivo.read())
llavePrivada = PKCS1_OAEP.new(key= llave)


mensaje = llavePrivada.decrypt(Recibir)
print(mensaje)

with open("mensajerecibido.txt","w+") as archivo:
    archivo.write(mensaje.decode('ascii'))


Mi_Socket.close()
print("DONE")

