"""
server.py

Este módulo contiene la definición y configuración del servidor HTTP para la aplicación de consulta de inmuebles.
Utiliza HTTPServer de la biblioteca http.server de Python y define InmuebleHandler como el manejador de solicitudes HTTP,
el cual está diseñado para responder a rutas específicas relacionadas con la consulta de inmuebles.

El servidor escucha en el puerto 8000 y está configurado para manejar solicitudes GET para obtener información sobre
inmuebles disponibles, aplicando diferentes filtros como estado, ciudad y año de construcción.

Cómo usar:
- Este archivo se debe ejecutar directamente como el punto de entrada principal de la aplicación.
- Una vez iniciado, el servidor escuchará las solicitudes HTTP en el puerto 8000.
- Las solicitudes a '/inmuebles' serán procesadas por InmuebleHandler para consultar y retornar datos de inmuebles.

Requisitos:
- Python 3.9 o superior.
- Biblioteca http.server de Python.
- Biblioteca mysql-connector-python para la conexión a la base de datos.
- Base de datos MySQL con la estructura y datos de la aplicación.
- Configuración de los datos de acceso a la base de datos en '.env'.
- Acceso a la base de datos configurado correctamente en 'db/db_connection.py'.

Ejemplo de ejecución:
$ python server.py
Esto inicia el servidor, que escucha en http://localhost:8000 esperando solicitudes.

"""

from http.server import HTTPServer
from handlers.inmueble_handler import InmuebleHandler

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, InmuebleHandler)
    print('Servidor iniciado, escuchando en el puerto 8000...')
    httpd.serve_forever()
