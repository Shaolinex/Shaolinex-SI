import Encriptar as Enc
from hashlib import md5

def feistelDecrypt(mensaje,llaves,ciclos):
    
    L3 = mensaje[0:mitad]
    R3 = mensaje[mitad::] 
    
    F4 = Enc.exor(L3,llaves[ciclos-1],mitad)
    L4 = Enc.exor(R3,F4,mitad)
    R4 = L3   
    mensaje2 = L4 + R4
        
    if ciclos > 1:
        return feistelDecrypt(mensaje2,llaves,ciclos-1)
    else:
        return mensaje2

def decode_binary_string(s): # Referenciado de: https://stackoverflow.com/questions/40557335/binary-to-string-text-in-python
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


archivo = open("mensajeSeguro.txt","r+",encoding="utf-8")
mensaje4 =  archivo.readlines()[0]
archivo.close()

mitad = len(mensaje4)//2

llave = []
archivo = open("keys.txt","r+")
for i in archivo:
    llave.append(i.strip().split("-"))
archivo.close()

mensaje3 = feistelDecrypt(mensaje4,llave,Enc.Vueltas)
mensaje3 = decode_binary_string(mensaje3)
print("mensaje desencriptado -->",mensaje3)


HashDesenc = md5()
HashDesenc.update(mensaje3.encode())
HashDesenc = HashDesenc.hexdigest()

if HashDesenc == Enc.HashEnc:
    print("El mensaje no ha sido adulterado")
else:
    print("La integridad del mensaje fue comprometida")