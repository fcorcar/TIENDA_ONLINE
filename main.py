from models.administrador import Administrador
from models.productos import Producto
from models.clientes import Cliente

admin = Administrador("Francisco", "TecnoMarket")

listado_productos = (
    Producto(1, "Televisión", 550.95, 50, "Electrónica", "https://www.worten.es/i/1ca9cf73308d37e572352b31571a051f13b1d2b4"),
    Producto(2, "Pc Gaming", 1560.25, 0, "Electrónica", "https://pcordenador.com/img/real/pc_gaming_rtx_5070_12gb__ryzen_5__16gb_ram.jpg"),
    Producto(3, "Mesita de noche", 45.00, 150, "Hogar", "https://img3.kenayhome.com/142502-large_default/rustic-mesita-de-noche-natural-3-cajones.jpg"),
    Producto(4, "Sofá", 360.99, 230, "Hogar", "https://sofaralia.com/wp-content/uploads/2024/04/sofaralia-sofa-chaiselongue-exytaiblle-ISABELLA.jpg")
)

listado_clientes = (
    Cliente(1, "Juan", "juan@gmail.com", True),
    Cliente(2, "Sara", "sara@gmail.com", False),
    Cliente(3, "Jose", "jose@gmail.com", True),
    Cliente(4, "Sofia", "sofia@gmail.com", False)
)

listado_clientes[1].agregar_pedido(10, (listado_productos[0], listado_productos[1]))
listado_clientes[1].agregar_pedido(11, (listado_productos[2], listado_productos[3]))
listado_clientes[2].agregar_pedido(12, (listado_productos[0],))
listado_clientes[3].agregar_pedido(13, (listado_productos[1], listado_productos[3]))