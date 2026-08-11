import psycopg2

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        # Se usa try-except para manejar errores
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                user="postgres",
                password="mateo2015",
                database="taller",
                port="5432"
            )
            print("Conectado a PostgreSQL")

        except Exception as e:
            print("Error de conexion:", e)

    def get_connection(self):
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexion cerrada")


db = Database()
db.connect()