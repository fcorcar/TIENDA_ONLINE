######################## IMPORTACIONES ########################
from dotenv import load_dotenv
import os


##################### CONFIGURACIONES #####################
# Carga las variables de entorno
load_dotenv()

# Devuelve la ruta donde estará la BD
def obtener_bd(nombre_bd:str) -> str:
    DB_URL = os.getenv(nombre_bd)
    return DB_URL
