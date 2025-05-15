class Producto:

    def __init__(self, id_producto:int, nombre:str, precio:float, stock:int, categoria:str, img_url:str):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__categoria = categoria
        self.__img_url = img_url


    @property
    def id_producto(self):
        return self.__id_producto

    @id_producto.setter
    def id_producto(self, valor):
        self.__id_producto = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        self.__stock = valor

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor

    @property
    def img_url(self):
        return self.__img_url

    @img_url.setter
    def img_url(self, valor):
        self.__img_url = valor

    
    @property
    def formato_dict(self): #Eso es lo que se sube a la bd
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "categoria": self.categoria,
            "imagen": self.img_url
        }
    



    