
from empleados import empleados_servicio


#Funcion para seleccionar el servicio
def seleccionar_servicio(cursor, placa):

    print("\n SELECCIÓN DE SERVICIO ")

    # Diccionario con servicios y precios
    servicios_menu = {
        "1": ("Cambio de aceite", 80000),
        "2": ("Alineación", 50000),
        "3": ("Revisión general", 100000),
        "4": ("Frenos", 120000),
        "5": ("Diagnóstico", 60000)
    }

    # Mostrar menú de servicios
    for key, value in servicios_menu.items():

        # key = número de opción
        # value[0] = nombre servicio
        # value[1] = costo
        print(f"{key}. {value[0]} - ${value[1]}")

    # Usuario selecciona opción
    op = input("Opción: ")

    # Validamos que exista
    if op not in servicios_menu:
        print("❌ Servicio inválido")
        return None, None

    # Guardamos nombre y costo del servicio
    tipo_servicio = servicios_menu[op][0]
    costo = servicios_menu[op][1]

    # Buscar automáticamente el empleado
    empleado = empleados_servicio[tipo_servicio]

    cursor.execute("""
        INSERT INTO servicios (tipo_servicio, costo, placa, empleado_id)
        VALUES (%s, %s, %s, %s)
    """, (
        tipo_servicio,
        costo,
        placa,
        empleado.id_empleado
    ))

    # Mostrar empleado asignado
    print("\n👨‍🔧 EMPLEADO ASIGNADO")
    print("Nombre:", empleado.nombre)
    print("Cargo:", empleado.cargo)
    print("Horario:", empleado.horario)

    # Retornamos datos
    return tipo_servicio, costo