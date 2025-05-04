class Administrador:

    def __init__(self, nombre:str, tienda:str):
        self.__nombre = nombre
        self.__tienda = tienda

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def tienda(self):
        return self.__tienda

    @tienda.setter
    def _tienda(self, valor):
        self.__tienda = valor
