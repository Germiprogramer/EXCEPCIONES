from correo import *
from comprobacion import *
import re

if __name__ == "__main__":
    usuario = input("identifiquese como usuario :")
    direccion = input("Identifique su dirección de correo :")
    
    correo = Correo(usuario, direccion)
    comprobacion(correo)