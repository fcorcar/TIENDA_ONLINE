from models.administrador import Administrador
from models.clientes import Cliente
from models.base_datos import base_datos

admin = Administrador("Francisco", "TecnoMarket")

# listado_productos = base_datos.buscar("productos")





# listado_clientes = [
#     Cliente(1, "Juan", "juan@gmail.com", True),
#     Cliente(2, "Sara", "sara@gmail.com", False),
#     Cliente(3, "Jose", "jose@gmail.com", True),
#     Cliente(4, "Sofia", "sofia@gmail.com", False)
# ]

# listado_clientes[1].agregar_pedido(10, (listado_productos[0], listado_productos[1]))
# listado_clientes[1].agregar_pedido(11, (listado_productos[2], listado_productos[3]))
# listado_clientes[2].agregar_pedido(12, (listado_productos[0],))
# listado_clientes[3].agregar_pedido(13, (listado_productos[1], listado_productos[3]))