# EXCEPCIONES

SE ha realizado un programa simulando la entrada de una dirección de correo electrónico.

# Clase Correo

    class Correo:
        def __init__(self, usuario, direccion):
            self.usuario = usuario
            self.direccion = direccion
        def get_usuario(self):
            return self.usuario
        def get_direccion(self):
            return self.direccion


# Funcion comprobacion

    def comprobacion(correo):
        buscararroba = re.search("@",correo.get_direccion())
        if buscararroba == None:
            print("Una dirección de correo debe contener un @, correo invalidado")
            print("reinicie el programa para introducir de nuevo el correo")
        else:
            es_seguracom = re.search(".com",correo.get_direccion())
            es_seguraes = re.search(".es",correo.get_direccion())
            if es_seguracom == None and es_seguraes == None:
                print("Cuenta bloqueada a causa de ataque")
                print("reinicie el programa para introducir de nuevo el correo")
            else:
                print("Bienvenido {}".format(correo.get_usuario()))
                
# Ejecucion del programa

    if __name__ == "__main__":
        usuario = input("identifiquese como usuario :")
        direccion = input("Identifique su dirección de correo :")

        correo = Correo(usuario, direccion)
        comprobacion(correo)


<img width="138" alt="2022-04-03 (2)" src="https://user-images.githubusercontent.com/91720991/161435717-b7663da6-3949-4bf0-95e3-632d58189cbb.png">
