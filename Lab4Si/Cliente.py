"""
Created on Wed Sep 29 09:30:01 2021

@author: Andres Ducaud / Marcela Linconao
"""

import socket

Host = "LocalHost"
Puerto = 8000

Mi_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Mi_Socket.connect((Host, Puerto))

Recibir = Mi_Socket.recv(1024)
Recibir = Recibir.decode(encoding = "ascii", errors = "ignore")
P,G,B = Recibir.split(",")

#print("Servidor: ", Recibir) Es solo para hacer pruebas, no hace falta imprimirlo

a = -1
while a > int(P) or a < 0:
    a = int(input(f"Ingrese un numero entre 0 y {int(P)} --> "))
    
A = (int(G)**a)%int(P)

Enviar = str(A)
Mi_Socket.send(Enviar.encode(encoding = "ascii", errors = "ignore"))

K = (int(B)**a)%int(P)
print(K) # Se imprime la llave para comprobar que son iguales
  
Mi_Socket.close()

