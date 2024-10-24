from fuerza_bruta.py import *

def test_fuerza_bruta():
    contraseña1 = "password"
    contraseña2 = "welcome123"

    assert calcula_sha(contraseña1) == "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    assert calcula_sha(contraseña2) == "a68349561396ec264a350847024a4521d00beaa3358660c2709a80f31c7acdd0"