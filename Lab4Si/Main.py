"""
Created on Wed Sep 29 09:30:01 2021

@author: Andres Ducaud / Marcela Linconao
"""

import os
from threading import Thread

def openCmd(comando):
    os.system("start /wait cmd /k "+str(comando))

Servidor = Thread(target = openCmd,args=["python Servidor.py"])
Cliente = Thread(target = openCmd,args=["python Cliente.py"])
Servidor.start()
Cliente.start()