from models.pedidos import Pedido

class Cliente:

    def __init__(self, id_cliente:int, nombre:str, email:str, estado:bool):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email
        self.__estado = estado
        self.__pedidos = []

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        self.__id_cliente = valor

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
        self.__pedidos.append(Pedido(id_pedido, self.id_cliente, lista_productos))

