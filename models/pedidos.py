from datetime import date

class Pedido:
    def __init__(self, id_pedido:int, id_usuario:int, lista_productos:list, fecha:str):
        self.__id_pedido = id_pedido
        self.__id_usuario = id_usuario
        self.__lista_productos = lista_productos
        # self.__total = sum(producto["precio"] for producto in lista_productos)
        self.__fecha = fecha

    @property
    def id_pedido(self):
        return self.__id_pedido

    @id_pedido.setter
    def id_pedido(self, valor):
        self.__id_pedido = valor

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        self.__id_usuario = valor

    @property
    def lista_productos(self):
        return self.__lista_productos

    @lista_productos.setter
    def lista_productos(self, valor):
        self.__lista_productos = valor

    # @property
    # def total(self):
    #     return self.__total

    # @total.setter
    # def total(self, valor):
    #     self.__total = valor

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        self.__fecha = valor

    
    @property
    def formato_dict(self): #Lo que se sube
        return {
            "id_usuario": self.id_usuario,
            "productos": self.lista_productos,
            "fecha": self.fecha
        }


    