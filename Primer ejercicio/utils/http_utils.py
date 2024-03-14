from urllib.parse import urlparse, parse_qs

def parse_query_params(path):
    """
    Analiza los parámetros de consulta de la URL proporcionada y los devuelve como un diccionario.

    Esta función es útil para extraer los parámetros de consulta de una URL en las solicitudes HTTP GET,
    transformándolos en un diccionario donde cada clave es el nombre del parámetro y cada valor es el valor del parámetro.

    Args:
        path (str): La URL completa desde la cual extraer los parámetros de consulta.

    Returns:
        dict: Un diccionario que contiene los parámetros de consulta parseados. Cada parámetro de consulta se devuelve
            como una entrada en el diccionario, con el valor del parámetro como una cadena de texto. Si un parámetro 
            aparece más de una vez en la URL, solo se devuelve su primer valor.
    """

    parsed_path = urlparse(path)
    query_params = parse_qs(parsed_path.query)
    return {k: v[0] for k, v in query_params.items()}

def validate_expected_params(query_params, expected_params):
    """
    Valida si los parámetros de consulta proporcionados contienen solo aquellos esperados.

    Esta función es útil para verificar si una solicitud HTTP contiene parámetros inesperados o no deseados,
    devolviendo una lista de todos los parámetros que no se encuentran entre los esperados.

    Args:
        query_params (dict): Un diccionario de parámetros de consulta para validar, donde cada clave es el nombre
                            del parámetro y cada valor es el valor del parámetro.
        expected_params (set): Un conjunto de cadenas que representan los nombres de los parámetros esperados.

    Returns:
        list: Una lista de nombres de parámetros de consulta que no están entre los esperados. La lista estará vacía
            si todos los parámetros de consulta proporcionados son esperados.
    """

    return [param for param in query_params if param not in expected_params]
