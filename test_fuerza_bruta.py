from fuerza_bruta import *

def test_fuerza_bruta():
    contraseña1 = "hOl4_bu3na5_t4RdeS"
    contraseña2 = "4Nd3sta3R8et1"

    assert calcula_sha(contraseña1) == "dd523a9b5e23cfdf71f445e5873842a1baaab4c17f493930929f182cb0b7fb17"
    assert calcula_sha(contraseña2) == "8a3edce1ec6610c03978a7a5d3923ceed966fa555d93614e87a7a3dac1c03099"