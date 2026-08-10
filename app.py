from conexio import Database
from cliente import Cliente
from vehiculos import registrar_vehiculo
from servicios import seleccionar_servicio


def conectar_bd():
    db = Database()
    db.connect()

    conexion = db.get_connection()
    cursor = conexion.cursor()

    print("\n===== REGISTRO COMPLETO =====")

    cliente = Cliente.registrar(cursor)

    vehiculo = registrar_vehiculo(cursor, cliente.documento)
    if vehiculo is None:
        return

    tipo_servicio, costo = seleccionar_servicio(cursor, vehiculo.placa)
    if tipo_servicio is None:
        return

    conexion.commit()

    print("\n✅ REGISTRO COMPLETO EXITOSO")
    print("Cliente:", cliente.nombre)
    print("Vehículo:", vehiculo.marca, vehiculo.modelo)
    print("Servicio:", tipo_servicio, "-", costo)

    db.close()