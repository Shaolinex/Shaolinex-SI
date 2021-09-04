from random import randint
import hashlib

'''

CANTIDAD DE VUELTAS PARA LA ENCRIPTACION Y DESENCRIPTACION

'''

Vueltas = 6

'''

CANTIDAD DE VUELTAS PARA LA ENCRIPTACION Y DESENCRIPTACION

'''
def exor(a,b,n): # Referenciado de; https://www.geeksforgeeks.org/feistel-cipher/     
    temp = ""     
    for i in range(n):      
        if (a[i] == b[i]):
            temp += "0"
        else: 
            temp += "1"    
            
    return temp 

def generarLlave(L): # Genero las llaves utilizadas para el exor con largo L
    llave = []
    for i in range(L):
        llave.append(str(randint(0,1)))
        
    return llave

def genLlaves(vueltas,mitad): # Genero una llave diferente para cada ciclo
    lista = []
    for i in range(vueltas):
        lista.append(generarLlave(mitad))
    
    return lista

def feistelEncrypt(mensaje,llaves,ciclos):
    mitad = len(mensaje)//2 # Calculo el largo de cada parte del mensaje
    if ciclos > 1:
        # Separo el mensaje
        L = mensaje[0:mitad]
        R = mensaje[mitad::]
        # Calculo la funcion
        F = exor(R,llaves[-ciclos],mitad)
        mensaje = R + exor(F,L,mitad) # R + L EXOR F
        
        return feistelEncrypt(mensaje,llaves,ciclos-1) #Si quedan cifrados por hacer vuelvo a llamar a la funcion
    else:
        # Separo el Mensaje
        L = mensaje[0:mitad]
        R = mensaje[mitad::]
        # Calculo la funcion
        F = exor(R,llaves[-ciclos],mitad) 
        mensaje = R + exor(F,L,mitad) # R + L EXOR F
         
        return mensaje

archivo = open("mensajeEntrada.txt","r+",encoding='utf-8')
palabra = archivo.readlines()[0]
archivo.close()



# Se calcula el hash de la palabra ingresada
HashEnc = hashlib.md5() 
HashEnc.update(palabra.encode())
HashEnc = HashEnc.hexdigest() 

palabra = [ord(i) for i in palabra] # Se transforman los caracteres a numeros
palabra = [format(i,"08b") for i in palabra] # Se transforman los numeros a binario
palabra = "".join(palabra) # Se une la lista de binarios en un string sin espacios

mitad = len(palabra)//2 # Se calcula la mitad del string, para separar las mitades



#### Se guarda el mensaje en formato binario luego de la sustitucion y permutacion

if __name__ == '__main__':
    llave = genLlaves(Vueltas,mitad) # Se generan x cantidad de llaves para el feistel
    llavesitas = llave.copy()
    
    for i in range(Vueltas):
        llavesitas[i] = "-".join(llavesitas[i])
        
    archivo = open("keys.txt","w+")
    archivo.writelines("\n".join(llavesitas))
    archivo.close()
    
    mensaje = feistelEncrypt(palabra,llave,Vueltas) # se llama la funcion de encriptacion, con el mensaje, las llaves y la cantidad de ciclos como parametros
    archivo = open("mensajeSeguro.txt","w+",encoding = "utf-8") 
    archivo.write(mensaje) 
    archivo.close()


    



    