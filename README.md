
# 🛒 TIENDA ONLINE

**TIENDA ONLINE** es una aplicación web desarrollada con Flask que simula la gestión de una tienda en línea. Permite visualizar productos, gestionar clientes y pedidos, y proporciona una interfaz clara y moderna para la administración.

## 🚀 Características

- **Catálogo de Productos**: Visualiza productos con imágenes, categorías, precios y disponibilidad de stock.
- **Gestión de Clientes**: Muestra información detallada de los clientes, incluyendo su estado (activo/inactivo) y número de pedidos realizados.
- **Pedidos**: Lista de pedidos con detalles como ID, cliente asociado, total y fecha.
- **Dashboard de Administración**: Información general del administrador, nombre de la tienda y fecha de inicio de sesión.
- **Estadísticas**:
  - Total de unidades en stock.
  - Número de clientes activos.
  - Cliente con más pedidos realizados.

## ⚙️ Tecnologías Utilizadas

- **Backend**: [Flask](https://flask.palletsprojects.com/)
- **Frontend**: HTML5, CSS3, Jinja2
- **Lenguaje**: Python 3.x

## 📁 Estructura del Proyecto

```
TIENDA_ONLINE/
├── app.py
├── main.py
├── models/
│   ├── basedatos.py
│   ├── clientes.py
│   ├── pedidos.py
│   └── administrador.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

## 🛠️ Instalación y Ejecución

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/fcorcar/TIENDA_ONLINE.git
   cd TIENDA_ONLINE
   ```

2. **Crear y activar un entorno virtual**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate 
   ```

3. **Instalar las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:

   ```bash
   python app.py
   ```

5. **Acceder a la aplicación**:

   Abre tu navegador y ve a `http://localhost:5000`

## 📌 Notas Adicionales

- Asegúrate de tener Python 3.x instalado en tu sistema.
- Las imágenes utilizadas en el catálogo deben estar ubicadas en la carpeta `static/images/`.
- Puedes personalizar los datos de productos, clientes y pedidos modificando los archivos correspondientes en la carpeta `models/`.

