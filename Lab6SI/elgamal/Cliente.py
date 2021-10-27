"""
Created on Wed Sep 29 09:30:01 2021

@author: Andres Ducaud / Marcela Linconao
"""
#%% 
import socket
from funciones import decrypt
from time import sleep


#%% Se inicia la conexion con el host

print("Cliente") # A veces no sabiamos que consola era que
Host = "LocalHost"
Puerto = 8000


Mi_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Mi_Socket.connect((Host, Puerto))


#%% Llave
def llaves(lista):
    q = int(lista[0].strip())
    key = int(lista[1].strip())
    p = int(lista[2].strip())
    return q,key,p

sleep(0.5)
with open("Llaves/keys.txt","r") as archivo:
    q,key,p = llaves(archivo.readlines())


#%% 
Recibir = Mi_Socket.recv(2048)

mensaje_seguro = Recibir.decode('ascii').split(" ")
mensaje_seguro = [int(x) for x in mensaje_seguro]

textoplano = decrypt(mensaje_seguro, p, key, q)
textoplano = ''.join(textoplano)
print(textoplano)
with open("mensajerecibido.txt","w+") as archivo:
    archivo.write(textoplano)
Mi_Socket.close()
print("DONE")

