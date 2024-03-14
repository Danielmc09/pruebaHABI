from http.server import BaseHTTPRequestHandler
import json
from services.consulta_inmuebles_service import get_inmuebles, NoContentError
from utils.http_utils import parse_query_params, validate_expected_params

class InmuebleHandler(BaseHTTPRequestHandler):
    """
    Handler para manejar las solicitudes HTTP relacionadas con los inmuebles.
    Extiende BaseHTTPRequestHandler y define cómo responder a las solicitudes GET.
    """
    
    def do_GET(self):
        """
        Maneja todas las solicitudes GET dirigidas al servidor.
        
        Si la ruta solicitada comienza con '/inmuebles', se procede a manejar la consulta
        de inmuebles. Cualquier otra ruta resulta en una respuesta 404 Not Found.
        """
        if self.path.startswith('/inmuebles'):
            self.handle_list_inmuebles()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def send_json_response(self, status_code, body):
        """
        Envía una respuesta JSON con el código de estado y cuerpo especificados.
        """
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())

    def handle_list_inmuebles(self):
        query_params = parse_query_params(self.path)
        expected_params = {'state', 'city', 'year_construction'}
        validation_errors = validate_expected_params(query_params, expected_params)

        if validation_errors:
            error_response = {
                "error": {
                    "code": 400,
                    "message": f"Parámetros inesperados: {', '.join(validation_errors)}."
                },
                "message": "Error en la solicitud."
            }
            self.send_json_response(400, error_response)
            return

        try:
            inmuebles = get_inmuebles(**query_params)
            success_response = {
                "data": inmuebles,
                "message": "Operación exitosa."
            }
            self.send_json_response(200, success_response)
        except NoContentError as e:
            success_response = {
                "data": [],
                "message": str(e)
            }
            self.send_json_response(200, success_response)
        except Exception as e:
            error_response = {
                "error": {
                    "code": 500,
                    "message": str(e)
                },
                "message": "Error en la solicitud."
            }
            self.send_json_response(500, error_response)
