######################## IMPORTACIONES ########################
from settings import obtener_bd
from pymongo import MongoClient



######################## CLASE ########################
class BaseDatos:

    def __init__(self, url_db:str, nombre_bd):
        self.cliente = MongoClient(url_db)
        self.db = self.cliente[nombre_bd]

    def insertar(self, nombre_tabla:str, datos:dict):
        self.db[nombre_tabla].insert_one(datos)

    def buscar(self, nombre_tabla:str):
        return list(self.db[nombre_tabla].find())
    

######################## INSTANCIAS ########################
base_datos = BaseDatos(obtener_bd("DB"), "TIENDA_ONLINE")
