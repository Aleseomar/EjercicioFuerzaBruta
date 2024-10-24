import hashlib

def calcula_sha(passwd: str):
    m = hashlib.sha256(passwd.encode())
    return m.hexdigest()
