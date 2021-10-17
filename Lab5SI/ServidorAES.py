"""
Created on Wed Sep 29 09:30:01 2021

@author: Andres Ducaud / Marcela Linconao
"""
#%% imports
import socket
import random
from Crypto.Cipher import AES

#%% Inicio del servidor
print("Servidor")
Host = "LocalHost"
Puerto = 8000

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((Host, Puerto))
Server.listen(1)
Conexion, Addr = Server.accept()
#%% Llave
kay = b"narcotraficantes" # Yo soy pablo emilio escobar gaviria XD

#%% DH
Primos =  [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661]
P = random.choice(Primos) # Publico
G = random.randint(0,P-1) # Publico
b = random.randint(0,P-1) # Secreto
B = (G**b)%P # Intercambiar

Enviar = str(P) + "," + str(G) + "," +str(B)
Conexion.send(Enviar.encode(encoding = "ascii", errors = "ignore"))
    
Recibir = Conexion.recv(1024)
Recibir = Recibir.decode(encoding = "ascii", errors = "ignore")
#print("Cliente: ", Recibir) Es solo para hacer pruebas no hace falta imprimirlo
    
K = (int(Recibir)**b)%P

# Recibe la llave del cliente
Recibir = Conexion.recv(1024)
Recibir = Recibir.decode(encoding = "ascii", errors = "ignore")

if K == int(Recibir): # Si las llaves coinciden envia el mensaje
    #%% Lectura mensaje
    print("Leyendo el mensaje...\n")
    archivo = open("mensajeentrada.txt","r+")
    lineas = archivo.readlines() # se lee el archivo
    archivo.close()
    
    lineas = "".join(lineas) # Se juntan las lineas
    lineas = lineas.encode("ASCII") # se transforman en bytes
    
    n = len(lineas)%16
    lineas = lineas+b' '*(16-n) if n!= 0 else lineas+b''
    
    aes = AES.new(kay, AES.MODE_ECB)   

    ciphertext = aes.encrypt(lineas)
    
    Conexion.send(ciphertext)
    print(lineas)
    print(ciphertext)
    print("Enviando mensaje Seguro...\n")
Conexion.close()
print("DONE")
