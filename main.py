from conexio import Database

def ejecutar_jenkins():
    db = Database()
    db.connect()

    print("Jenkins ejecutó el proyecto correctamente")

    if db.get_connection():
        db.close()


if __name__ == "__main__":
    ejecutar_jenkins()