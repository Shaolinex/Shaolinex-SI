"""
Created on Wed Sep 29 09:30:01 2021

@author: Andres Ducaud / Marcela Linconao
"""
#%% 
import socket
import random
from Crypto.Cipher import DES
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
#%% Llaves
key1 = b'chiritos' # Llave para des
key2 = b'cachupin' # Llave para 3des
key3 = b'apodador' # Llave para 3des

#%% DH

Recibir = Mi_Socket.recv(1024)
Recibir = Recibir.decode(encoding = "ascii", errors = "ignore")
P,G,B = Recibir.split(",") # El numero primo, G y el numero de bob

a = random.randint(1,int(P)-1) # Se determina el numero secreto de Alice
A = (int(G)**a)%int(P) # Se calcula el numero a intercambiar con bob

Enviar = str(A)
Mi_Socket.send(Enviar.encode(encoding = "ascii", errors = "ignore"))

K = (int(B)**a)%int(P)

#%% Autenticar la llave para la recepcion del mensaje
Enviar = str(K)
Mi_Socket.send(Enviar.encode(encoding = "ascii", errors = "ignore"))

try: # en caso de que no exista respuesta del servidor se finaliza
    Recibir = Mi_Socket.recv(1024)
    
    #%% DES
    #'''
    '''
    print("Desencriptando mensaje con DES...\n") # usado para testear el codigo
    des = DES.new(key1, DES.MODE_ECB) # Se crea un objeto para usar DES
    
    textoplano = des.decrypt(Recibir) # Se desencrypta el mensaje
    
    '''
    #%% 3DES
    print("Desencriptando mensaje con 3DES...\n") # usado para testear el codigo
    des1 = DES.new(key1, DES.MODE_ECB)
    des2 = DES.new(key2, DES.MODE_ECB)
    des3 = DES.new(key3, DES.MODE_ECB)
    
    textoplano = des1.decrypt(Recibir)
    textoplano = des2.encrypt(Recibir)
    textoplano = des3.decrypt(Recibir)
    
    
    #%%
    #print(Recibir)
    #print(textoplano)
    print("Escribiendo el resultado...\n") # Los puntos son para mas tension owo
    textoplano = quitarPadding(textoplano) 
    
    archivo = open('mensajerecibido.txt','w+') # Se escribe el mensaje traducido
    archivo.writelines(textoplano.decode('ascii'))
    archivo.close()
    
except:
    pass

Mi_Socket.close()
print("DONE") # Se ve lindo este print al final del codigo :D

