from flask import Flask, render_template, request
from datetime import date, datetime
from models.productos import Producto
from models.usuarios import Usuario
from models.base_datos import base_datos
from models.pedidos import Pedido
from bson import ObjectId

from models.administrador import Administrador

app = Flask(__name__)

admin = Administrador("Francisco", "TecnoMarket")
# usuarios = base_datos.obtener("usuarios", Usuario) # Crea un pedido, se implementa en la version del cliente
# usuarios[2].realizar_pedido()


@app.errorhandler(404)
def error404(error):
    return render_template("404.html"), 404

@app.route("/")
def panel_control():
    # Bienvenida
    kwargs = {
        "nombre_admin": admin.nombre,
        "tienda": admin.tienda,
        "fecha": date.today()
    }

    # Productos
    listado_productos = base_datos.obtener_ultimos("productos", Producto, 6)

    # Usuarios
    listado_usuarios = base_datos.obtener_ultimos("usuarios", Usuario, 3)

    # Pedidos
    if request.method == "POST":
        id_pedido = request.form["id"]
        pedido = base_datos.obtener("pedidos", Pedido, {"_id": ObjectId(id_pedido)})
        ids_prod = [ObjectId(id_str) for id_str in pedido[0].lista_productos]
        productos = base_datos.obtener("productos", Producto, {"_id": {"$in": ids_prod}})
        return render_template("productos.html", titulo_pr=f"Productos del pedido '{id_pedido}'", listado_productos=productos)

    listado_pedidos = base_datos.obtener_ultimos("pedidos", Pedido, 3)

    return render_template("dashboard.html", **kwargs, titulo_pr="Productos añadidos recientemente", listado_productos=listado_productos, titulo_us="Usuarios registrados recientemente", listado_usuarios=listado_usuarios, titulo_pe=f"Últimos pedidos", listado_pedidos=listado_pedidos)

@app.route("/añadir-producto", methods=["GET", "POST"])
def añadir_producto():
    if request.method == "POST":
        producto = Producto(0,**request.form)

        exito = base_datos.insertar("productos", producto.formato_dict)
        mensaje = ""

        if exito: mensaje = "Producto añadido con éxito."
        else: mensaje = "El producto no se ha podido añadir."

        return render_template("añadir_producto.html", mensaje=mensaje)

    return render_template("añadir_producto.html")


@app.route("/productos")
def productos():
    listado_productos = base_datos.obtener("productos", Producto)
    total_stock = sum(producto.stock for producto in listado_productos)

    return render_template("productos.html", titulo_pr=f"Catálogo de productos (Stock total: {total_stock})", listado_productos=listado_productos)


@app.route("/productos/<id_producto>")
def producto_especifico(id_producto):
    listado_productos = base_datos.obtener("productos", Producto)

    for prod in listado_productos:
        if str(prod.id_producto) == id_producto.strip():
            return render_template("detalle_producto.html", producto=prod)
    
    else:
        return render_template("404.html"), 404


@app.route("/registrar-usuarios", methods=["GET", "POST"])
def registrar_usuarios():
    if request.method == "POST":
        usuario = Usuario(0, datetime.now(),**request.form)

        exito = base_datos.insertar("usuarios", usuario.formato_dict)
        mensaje = ""

        if exito: mensaje = "Usuario registrado con éxito."
        else: mensaje = "El usuario no se ha podido registrar."

        return render_template("registro_usuarios.html", mensaje=mensaje)

    return render_template("registro_usuarios.html")


@app.route("/usuarios")
def usuarios():
    listado_usuarios = base_datos.obtener("usuarios", Usuario)
    usuarios_activos = sum(1 for usuario in listado_usuarios if usuario.estado)

    return render_template("usuarios.html", titulo_us=f"Usuarios (Activos: {usuarios_activos})", listado_usuarios=listado_usuarios)


@app.route("/pedidos", methods=["GET", "POST"])
def pedidos():
    if request.method == "POST":
        id_pedido = request.form["id"]
        pedido = base_datos.obtener("pedidos", Pedido, {"_id": ObjectId(id_pedido)})
        ids_prod = [ObjectId(id_str) for id_str in pedido[0].lista_productos]
        productos = base_datos.obtener("productos", Producto, {"_id": {"$in": ids_prod}})
        return render_template("productos.html", titulo_pr=f"Productos del pedido '{id_pedido}'", listado_productos=productos)

    listado_pedidos = base_datos.obtener("pedidos", Pedido)
    return render_template("pedidos.html", titulo_pe=f"Pedidos", listado_pedidos=listado_pedidos)



if __name__ == "__main__":
    app.run(debug=True)