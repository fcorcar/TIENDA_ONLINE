from models.pedidos import Pedido
from datetime import date, datetime
from models.base_datos import base_datos

class Usuario:

    def __init__(self, id_usuario:int, fecha_registro:str, nombre:str, email:str, contraseña:str):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__email = email
        self.__contraseña = contraseña
        self.__fecha_registro = fecha_registro
        self.__estado = True #añadir aleatorio
        self.__carrito = ["682658d17079f8b17d9e6f85", "68265ae0787592c74399edc3"] #Guada los productos que se añadiran al pedido

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
    def carrito(self):
        return self.__carrito

    @carrito.setter
    def carrito(self, valor):
        self.__carrito = valor


    def realizar_pedido(self):
        # Creo el objeto del pedido
        pedido = Pedido(0, self.id_usuario, self.carrito, datetime.now())

        #Subo el pedido
        base_datos.insertar("pedidos", pedido.formato_dict)



    @property
    def formato_dict(self): #Eso es lo que se sube a la bd
        return {
            "fecha_registro": self.fecha_registro,
            "nombre": self.nombre,
            "email": self.email,
            "contraseña": self.contraseña
        }
