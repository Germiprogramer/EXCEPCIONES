import re

class Correo:
    def __init__(self, usuario, direccion):
        self.usuario = usuario
        self.direccion = direccion
    def get_usuario(self):
        return self.usuario
    def get_direccion(self):
        return self.direccion
