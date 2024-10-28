import hashlib

def calcula_sha(passwd: str):
    m = hashlib.sha256(passwd.encode())
    return m.hexdigest()

def comparacion_sha(passwd:str,archivo:str)->bool:
    with open(archivo,'r') as f:
        contenido = f.read()
        contenido_sha=calcula_sha(contenido)
        if(contenido_sha==passwd):
            return True
        else:
            return False

if __name__=='__main__':
   print (comparacion_sha(calcula_sha('root'),'contrasenas_test.txt'))

