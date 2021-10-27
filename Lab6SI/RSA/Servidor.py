"""
Created on Wed Sep 29 09:30:01 2021

@author: Andres Ducaud / Marcela Linconao
"""
#%% imports
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#%% Inicio del servidor
print("Servidor")
Host = "LocalHost"
Puerto = 8000

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((Host, Puerto))
Server.listen(1)
Conexion, Addr = Server.accept()

#%% llave

key = RSA.generate(1024)
with open("llaves/keys.pem","wb") as archivo:
    archivo.write(key.exportKey('PEM'))
    
#%% 
print("Leyendo el mensaje...\n")
with open("mensajeentrada.txt","r+") as archivo:
    texto = [x.strip() for x in archivo]
    texto = " ".join(texto)

texto = texto.encode('ascii')

print("Enviando mensaje Seguro...\n")
public_key = PKCS1_OAEP.new(key.publickey())
mensaje_seguro = public_key.encrypt(texto)
print(mensaje_seguro)

Conexion.send(mensaje_seguro)


Conexion.close()
print("DONE")
