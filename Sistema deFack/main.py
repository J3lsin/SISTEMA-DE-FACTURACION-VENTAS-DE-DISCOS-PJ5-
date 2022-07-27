
from flask import Flask, render_template, request, redirect, flash,session
import controlador_disco
import controlador_ventas

from bd import obtener_conexion

app = Flask(__name__)
app.secret_key = "esta es la clve secreta"
"""
Definición de rutas
"""


@app.route("/agregar_juego")
def formulario_agregar_juego():
    return render_template("agregar_juego.html")


@app.route("/guardar_juego", methods=["POST"])
def guardar_juego():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_disco.insertar_juego(nombre, descripcion, precio)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/juegos")


@app.route("/")
@app.route("/juegos")
def juegos():
    juegos = controlador_disco.obtener_juegos()
    return render_template("discos.html", juegos=juegos)


@app.route("/eliminar_juego", methods=["POST"])
def eliminar_juego():
    controlador_disco.eliminar_juego(request.form["id"])
    return redirect("/juegos")


@app.route("/formulario_editar_juego/<int:id>")
def editar_juego(id):
    # Obtener el juego por ID
    juego = controlador_disco.obtener_juego_por_id(id)
    return render_template("editar_juego.html", juego=juego)


@app.route("/actualizar_juego", methods=["POST"])
def actualizar_juego():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_disco.actualizar_juego(nombre, descripcion, precio, id)
    return redirect("/juegos")


def valid_login(usuario,pws):

    conexion = obtener_conexion()
   
    sql  = "SELECT id, usuario, nombres FROM usuarios WHERE usuario = %s AND pws = %s"
    dsUser = None
    with conexion.cursor() as cursor:
        cursor.execute(sql, (usuario,pws))
        dsUser = cursor.fetchone()
    conexion.close()
    return dsUser

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['usuario'],
                       request.form['pws']):
            session["usuario"] = request.form['usuario']
            session["logged"] = True

            return redirect("/juegos")
        else:
            error = 'Invalid username/password'
            
    session["logged"] = False

    return render_template('login.html', error=error)


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    session.pop("logged", None)
    return redirect("/login")

@app.route("/agregar_venta")
def formulario_agregar_venta():
    juegos_en_venta = controlador_disco.obtener_juegos()
    tipo_comprobantes = controlador_ventas.obtener_tipos_de_comprobante()
    return render_template("agregar_venta.html", juegos_en_venta=juegos_en_venta, tipo_comprobantes=tipo_comprobantes)
    

@app.route("/guardar_venta", methods=["POST"])
def guardar_venta():
    id_tipo_comprobante = request.form["id_tipo_comprobante"]
    fecha = request.form["fecha"]
    name_c = request.form["name_c"]
    direccion = request.form["direccion"]
    id_pj5 = request.form["id_pj5"]
    cantidad = request.form["cantidad"]

    controlador_ventas.insertar_venta(id_tipo_comprobante, fecha, name_c , direccion, id_pj5, cantidad)

    return redirect("/ventas")


@app.route("/ventas")
def ventas():
    ventas = controlador_ventas.obtener_ventas()
    return render_template("ventas.html", ventas=ventas)


@app.route("/eliminar_venta", methods=["POST"])
def eliminar_venta():
    controlador_ventas.eliminar_venta(request.form["id"])
    return redirect("/ventas")

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
