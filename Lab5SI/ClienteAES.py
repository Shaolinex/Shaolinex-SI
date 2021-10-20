"""
Created on Wed Sep 29 09:30:01 2021

@author: Andres Ducaud / Marcela Linconao
"""
#%% 
import socket
import random
from Crypto.Cipher import AES

#%% Funcion para eliminar el padding
def quitarPadding(texto):
    contador = 0
    for i in range(1,len(texto)+2):
        if texto[-i] == 32: # b' ' es 32, que es el byte utilizado para padding
            contador +=1
        else:
            break
    return texto[0:len(texto)-contador]
#%% Se inicia la conexion con el host
print("Cliente") # A veces no sabiamos que consola era que
Host = "LocalHost"
Puerto = 8000

Mi_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Mi_Socket.connect((Host, Puerto))
#%% Llave
kay = b"narcotraficantes" # Yo soy pablo emilio escobar gaviria XD

#%%  DH
Recibir = Mi_Socket.recv(1024)
Recibir = Recibir.decode(encoding = "ascii", errors = "ignore")
P,G,B = Recibir.split(",")


a = random.randint(1,int(P)-1)
A = (int(G)**a)%int(P)

Enviar = str(A)
Mi_Socket.send(Enviar.encode(encoding = "ascii", errors = "ignore"))

K = (int(B)**a)%int(P)

#%% Autenticar la llave para la recepcion del mensaje
Enviar = str(K)
Mi_Socket.send(Enviar.encode(encoding = "ascii", errors = "ignore"))

try: # en caso de que no exista respuesta del servidor se finaliza
    Recibir = Mi_Socket.recv(1024)
    
    print("Desencriptando mensaje con AES...\n") # usado para testear el codigo
    
    cipher = AES.new(kay, AES.MODE_ECB) 
    textoplano = cipher.decrypt(Recibir)

    print("Escribiendo el resultado...\n") # Los puntos son para mas tension owo
    textoplano = quitarPadding(textoplano) 
    print(textoplano)
    archivo = open('mensajerecibido.txt','w+') # Se escribe el mensaje traducido
    archivo.writelines(textoplano.decode('ascii'))
    archivo.close()
except:
    pass
  
Mi_Socket.close()
print("DONE")

