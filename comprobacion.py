from correo import *
import re

usuario = input("identifiquese como usuario :")
direccion = input("Identifique su dirección de correo :")

correo = Correo(usuario, direccion)

def comprobacion(correo):
    buscararroba = re.search("@",correo.get_direccion())
    if buscararroba == None:
        print("Una dirección de correo debe contener un @, correo invalidado")
        print("reinicie el programa para introducir de nuevo el correo")
    else:
        pass
    es_seguracom = re.search(".com",correo.get_direccion())
    es_seguraes = re.search(".es",correo.get_direccion())
    if es_seguracom == None and es_seguraes == None:
        print("Cuenta bloqueada a causa de ataque")
    else:
        print("Bienvenido {}".format(correo.get_usuario()))

comprobacion(correo)

