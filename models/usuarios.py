from models.pedidos import Pedido

class Usuario:

    def __init__(self, id_usuario:int, nombre:str, email:str, contraseña:str, fecha_registro:str):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__email = email
        self.__contraseña = contraseña
        self.__fecha_registro = fecha_registro
        self.__estado = True #añadir aleatorio
        self.__pedidos = []

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        self.__id_usuario = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, valor):
        self.__contraseña = valor

    @property
    def fecha_registro(self):
        return self.__fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, valor):
        self.__fecha_registro = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def pedidos(self):
        return self.__pedidos

    @pedidos.setter
    def pedidos(self, valor):
        self.__pedidos = valor


    def agregar_pedido(self, id_pedido:int, lista_productos:list):
        self.__pedidos.append(Pedido(id_pedido, self.id_usuario, lista_productos))

    @property
    def formato_dict(self): #Eso es lo que se sube a la bd
        return {
            "nombre": self.nombre,
            "email": self.email,
            "contraseña": self.contraseña,
            "fecha_registro": self.fecha_registro
        }
