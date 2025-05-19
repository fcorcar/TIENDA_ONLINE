######################## IMPORTACIONES ########################
from settings import obtener_bd
from pymongo import MongoClient, DESCENDING



######################## CLASE ########################
class BaseDatos:

    def __init__(self, url_db:str, nombre_bd):
        try:
            self.cliente = MongoClient(url_db)
            self.db = self.cliente[nombre_bd]
            print("Conectado a MongoDB con éxito.")

        except Exception as e:
            print("Error! No ha sido posible la conexión a MongoDB.", e)


    def insertar(self, nombre_tabla:str, datos:dict):
        try:
            resultado = self.db[nombre_tabla].insert_one(datos)

            if resultado.inserted_id:
                print("Insertado con éxito.")
                return True
            else:
                print("Error! No se ha podido insertar.")
                return False
            
        except Exception as e:
            print("Error! No se ha podido insertar.", e)
            return False


    def obtener(self, nombre_tabla:str, clase:object, filtro: dict = None):
        return [clase(*diccionario.values()) for diccionario in list(self.db[nombre_tabla].find(filtro))]
    

    def obtener_ultimos(self, nombre_tabla:str, clase:object, num:int):
        return [clase(*diccionario.values()) for diccionario in list(self.db[nombre_tabla].find().sort('_id', DESCENDING).limit(num))]

######################## INSTANCIAS ########################
base_datos = BaseDatos(obtener_bd("DB"), "TIENDA_ONLINE")
