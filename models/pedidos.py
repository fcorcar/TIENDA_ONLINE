from datetime import date

class Pedido:
    def __init__(self, id_pedido:int, id_cliente:int, lista_productos:list):
        self.__id_pedido = id_pedido
        self.__id_cliente = id_cliente
        self.__lista_productos = lista_productos
        self.__total = sum(producto.precio for producto in lista_productos)
        self.__fecha = date.today()

    @property
    def id_pedido(self):
        return self.__id_pedido

    @id_pedido.setter
    def id_pedido(self, valor):
        self.__id_pedido = valor

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        self.__id_cliente = valor

    @property
    def lista_productos(self):
        return self.__lista_productos

    @lista_productos.setter
    def lista_productos(self, valor):
        self.__lista_productos = valor

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, valor):
        self.__total = valor

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        self.__fecha = valor


    