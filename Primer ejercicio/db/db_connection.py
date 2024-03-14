from typing import ContextManager
import mysql.connector
from mysql.connector.connection_cext import CMySQLConnection
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def get_db_connection() -> ContextManager[CMySQLConnection]:
    """
    Establece y devuelve una conexión a la base de datos MySQL.

    :return: Una instancia de ContextManager que gestiona la conexión con la base de datos.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar con la base de datos: {err}")
        raise
