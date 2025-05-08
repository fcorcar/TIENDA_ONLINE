from flask import Flask, render_template, request, redirect
from main import admin, listado_productos, listado_clientes
from datetime import date
from models.productos import Producto

app = Flask(__name__)

@app.route("/")
def inicio():
    kwargs = {
        "pagina": "inicio",
        "nombre_admin": admin.nombre,
        "tienda": admin.tienda,
        "fecha": date.today()
    }
    
    return render_template("dashboard.html", **kwargs)

@app.route("/catalogo")
def catalogo():
    total_stock = sum(producto.stock for producto in listado_productos)
    return render_template("dashboard.html", pagina="catalogo", listado_productos=listado_productos, total_stock=total_stock)

@app.route("/clientes")
def clientes():
    clientes_activos = sum(1 for cliente in listado_clientes if cliente.estado)

    cliente_top = ""
    max_pedidos = -1

    for cliente in listado_clientes:
        num_pedidos = len(cliente.pedidos)
        if num_pedidos > max_pedidos:
            max_pedidos = num_pedidos
            cliente_top = cliente.nombre

    return render_template("dashboard.html", pagina="clientes", listado_clientes=listado_clientes, clientes_activos=clientes_activos, cliente_top=cliente_top)

@app.route("/pedidos")
def pedidos():
    suma_total = sum(pedido.total for cliente in listado_clientes for pedido in cliente.pedidos)        
    return render_template("dashboard.html", pagina="pedidos", listado_clientes=listado_clientes, suma_total=suma_total)

@app.route("/añadir-producto", methods=["GET", "POST"])
def añadir_producto():   
    if request.method == "POST":
        id_producto = 0
        nombre_producto = request.form["nombre"]
        precio_producto = float(request.form["precio"])
        stock_producto = int(request.form["stock"])
        categoria_producto = request.form["categoria"]
        imagen_producto = request.form["url_imagen"]

        if listado_productos: id_producto = listado_productos[-1].id_producto + 1
        else: id_producto = 1
            
        listado_productos.append(Producto(id_producto, nombre_producto, precio_producto, stock_producto, categoria_producto, imagen_producto))

        return redirect("/catalogo")
    return render_template("dashboard.html", pagina="añadir-producto")


if __name__ == "__main__":
    app.run(debug=True)