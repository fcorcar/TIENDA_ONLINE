from models.pedidos import Pedido
from datetime import datetime
from models.base_datos import base_datos
import random

class Usuario:

    def __init__(self, id_usuario:int, fecha_registro:str, nombre:str, email:str, contraseña:str):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__email = email
        self.__contraseña = contraseña
        self.__fecha_registro = fecha_registro
        self.__estado = random.choice([True, False]) # Se implementaría con la versión del cliente
        self.__carrito = ["6826609b787592c74399edca",] #Guada los productos que se añadirán al pedido

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
        pedido = Pedido(0, self.id_usuario, self.carrito, 0, datetime.now())
        base_datos.insertar("pedidos", pedido.formato_dict)


    @property
    def formato_dict(self):
        return {
            "fecha_registro": self.fecha_registro,
            "nombre": self.nombre,
            "email": self.email,
            "contraseña": self.contraseña
        }
