from bd import obtener_conexion
from arrow import utcnow, get
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import black, purple, white
from reportlab.pdfgen import canvas
def insertar_venta(id_tipo_comprobante, fecha, name_c, direccion, id_pj5, cantidad):
    conexion = obtener_conexion()
    sql = "INSERT INTO Ventas(id_tipo_comprobante, fecha, name_c, direccion, id_pj5, cantidad) VALUES (%s, %s, %s, %s, %s, %s)"
    conexion.cursor().execute(sql,(id_tipo_comprobante, fecha, name_c, direccion, id_pj5, cantidad));
    conexion.commit()
    conexion.close()


def obtener_ventas():
    conexion = obtener_conexion()
    ventas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT ventas.id, tipo_comprobante.descripcion, fecha, name_c, direccion, juegos.nombre, cantidad FROM ventas inner join juegos on ventas.id_pj5 =juegos.id inner join tipo_comprobante on ventas.id_tipo_comprobante = tipo_comprobante.id;")
        ventas = cursor.fetchall()
    conexion.close()
    return ventas


def eliminar_venta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM ventas WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_venta_por_id(id):
    conexion = obtener_conexion()
    venta = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, id_tipo_comprobante, fecha, name_c, direccion, id_pj5, cantidad FROM ventas WHERE id = %s", (id,))
        venta = cursor.fetchone()
    conexion.close()
    return venta

def obtener_tipos_de_comprobante():
    conexion = obtener_conexion()
    tipos_de_comprobante = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, descripcion FROM tipo_comprobante")
        
        tipos_de_comprobante = cursor.fetchall()
    conexion.close()
    return tipos_de_comprobante


class reportePDF(object):

 def generarReporte():
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    conexion = obtener_conexion()
    conexion.row_factory = dict_factory 
    cursor = conexion.cursor()

    cursor.execute("SELECT juegos,tipo_comprobante,usuarios,ventas FROM giosre")
    datos = cursor.fetchall()


    conexion.close()

    titulo = "LISTADO DE USUARIOS"

    cabecera = (
        ("juegos", "juegos"),
        ("tipo_comprobante", "tipo_comprobante"),
        ("usuarios", "usuarios"),
        ("ventas", "ventas"),
        )

    nombrePDF = "Listado de usuarios.pdf"

    reporte = reportePDF(titulo, cabecera, datos, nombrePDF).Exportar()
    print(reporte)