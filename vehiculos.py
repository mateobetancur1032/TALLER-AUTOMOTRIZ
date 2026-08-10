class Vehiculo:
    def __init__(self, placa, marca, modelo, ano, kilometraje):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.kilometraje = kilometraje


class Carro(Vehiculo):
    def __init__(self, placa, marca, modelo, ano, kilometraje, puertas):
        super().__init__(placa, marca, modelo, ano, kilometraje)
        self.puertas = puertas


class Moto(Vehiculo):
    def __init__(self, placa, marca, modelo, ano, kilometraje, tipo):
        super().__init__(placa, marca, modelo, ano, kilometraje)
        self.tipo = tipo


def registrar_vehiculo(cursor, documento_cliente):
    print("\n DATOS DEL VEHÍCULO ")
    print("1. Carro")
    print("2. Moto")

    opcion = input("Seleccione tipo: ")

    placa = input("Placa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = input("Año: ")
    kilometraje = input("Kilometraje: ")

    if opcion == "1":
        puertas = input("Número de puertas: ")
        vehiculo = Carro(placa, marca, modelo, ano, kilometraje, puertas)
        tipo_bd = "carro"

    elif opcion == "2":
        tipo_moto = input("Tipo de moto: ")
        vehiculo = Moto(placa, marca, modelo, ano, kilometraje, tipo_moto)
        tipo_bd = "moto"

    else:
        print("❌ Tipo inválido")
        return None

    cursor.execute("""
        INSERT INTO vehiculos (placa, marca, modelo, ano, kilometraje, documento, tipo_vehiculo)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        vehiculo.placa,
        vehiculo.marca,
        vehiculo.modelo,
        vehiculo.ano,
        vehiculo.kilometraje,
        documento_cliente,
        tipo_bd
    ))

    return vehiculo