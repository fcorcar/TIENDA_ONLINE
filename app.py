from flask import Flask, render_template, request, redirect
from main import admin
from datetime import date, datetime
from models.productos import Producto
from models.usuarios import Usuario
from models.base_datos import base_datos

app = Flask(__name__)

@app.errorhandler(404)
def error404(error):
    return render_template("404.html"), 404

@app.route("/")
def panel_control():
    kwargs = {
        "nombre_admin": admin.nombre,
        "tienda": admin.tienda,
        "fecha": date.today()
    }
    
    return render_template("dashboard.html", **kwargs)


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
    return render_template("productos.html", listado_productos=listado_productos, total_stock=total_stock)


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

    usuario_top = ""
    max_pedidos = -1

    for usuario in listado_usuarios:
        num_pedidos = len(usuario.pedidos)
        if num_pedidos > max_pedidos:
            max_pedidos = num_pedidos
            usuario_top = usuario.nombre

    return render_template("usuarios.html", listado_usuarios=listado_usuarios, usuarios_activos=usuarios_activos, usuario_top=usuario_top)


# @app.route("/")
# def inicio():
#     kwargs = {
#         "pagina": "inicio",
#         "nombre_admin": admin.nombre,
#         "tienda": admin.tienda,
#         "fecha": date.today()
#     }
    
#     return render_template("dashboard.html", **kwargs)

# @app.route("/catalogo")
# def catalogo():
#     listado_productos = base_datos.buscar("productos")

#     total_stock = sum(producto["stock"] for producto in listado_productos)
#     return render_template("dashboard.html", pagina="catalogo", listado_productos=listado_productos, total_stock=total_stock)

# @app.route("/clientes")
# def clientes():
#     clientes_activos = sum(1 for cliente in listado_clientes if cliente.estado)

#     cliente_top = ""
#     max_pedidos = -1

#     for cliente in listado_clientes:
#         num_pedidos = len(cliente.pedidos)
#         if num_pedidos > max_pedidos:
#             max_pedidos = num_pedidos
#             cliente_top = cliente.nombre

#     return render_template("dashboard.html", pagina="clientes", listado_clientes=listado_clientes, clientes_activos=clientes_activos, cliente_top=cliente_top)

# @app.route("/pedidos")
# def pedidos():
#     suma_total = sum(pedido.total for cliente in listado_clientes for pedido in cliente.pedidos)        
#     return render_template("dashboard.html", pagina="pedidos", listado_clientes=listado_clientes, suma_total=suma_total)

# @app.route("/añadir-producto", methods=["GET", "POST"])
# def añadir_producto():   
#     if request.method == "POST":
#         producto = Producto(0, request.form["nombre"], float(request.form["precio"]), int(request.form["stock"]), request.form["categoria"], request.form["url_imagen"])
        
#         producto_dict = {
#             "nombre": producto.nombre,
#             "precio": producto.precio,
#             "stock": producto.stock,
#             "categoria": producto.categoria,
#             "imagen": producto.img_url
#         }

#         base_datos.insertar("productos", producto_dict)

#         return redirect("/catalogo")
#     return render_template("dashboard.html", pagina="añadir-producto")


if __name__ == "__main__":
    app.run(debug=True)