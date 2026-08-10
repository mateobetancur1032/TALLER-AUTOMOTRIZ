class Cliente:
    def __init__(self, documento, nombre, telefono, correo):
        self.documento = documento
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    @staticmethod
    def registrar(cursor):
        print("\n DATOS DEL CLIENTE ")

        documento = input("Documento: ")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")

        cliente = Cliente(documento, nombre, telefono, correo)

        cursor.execute("""
            INSERT INTO clientes (documento, nombre, telefono, correo)
            VALUES (%s, %s, %s, %s)
        """, (
            cliente.documento,
            cliente.nombre,
            cliente.telefono,
            cliente.correo
        ))

        return cliente