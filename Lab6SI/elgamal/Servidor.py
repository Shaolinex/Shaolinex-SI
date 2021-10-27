"""
Created on Wed Sep 29 09:30:01 2021

@author: Andres Ducaud / Marcela Linconao
"""
#%% imports
import socket
import random
from funciones import gen_key,power,encrypt

#%% Inicio del servidor
print("Servidor")
Host = "LocalHost"
Puerto = 8000

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((Host, Puerto))
Server.listen(1)
Conexion, Addr = Server.accept()

#%% valores
a = random.randint(2, 10)
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
    
key = gen_key(q)# llave privada para el cliente

    
#%% 

print("Leyendo el mensaje...\n")
with open("mensajeentrada.txt","r+") as archivo:
    texto = [x.strip() for x in archivo]
    texto = " ".join(texto)

h = power(g, key, q)
print("Enviando mensaje Seguro...\n")
mensaje_seguro, p = encrypt(texto, q, h, g)

mensaje_seguro = [str(x) for x in mensaje_seguro]

mensaje_seguro = " ".join(mensaje_seguro).encode('ascii')

with open("Llaves/keys.txt","w+") as archivo:
    archivo.write(str(q))
    archivo.write('\n'+str(key))
    archivo.write('\n'+str(p))

Conexion.send(mensaje_seguro)

Conexion.close()
print("DONE")
