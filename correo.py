import re

class Correo:
    def __init__(self, usuario, direccion):
        self.usuario = input("Identifiquese :")
        self.direccion = input("Escriba el correo :")
    def get_direccion(self):
        return self.direccion
