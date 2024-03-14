from typing import List, Optional, Dict, Any
from mysql.connector.connection_cext import CMySQLConnection
from db.db_connection import get_db_connection

class NoContentError(Exception):
    """Excepción para cuando no se encuentran contenidos."""
    pass

def get_inmuebles(
    state: Optional[str] = None,
    city: Optional[str] = None,
    year_construction: Optional[int] = None
) -> List[Dict[str, Any]]:
    """
    Obtiene una lista de inmuebles filtrada por los parámetros proporcionados.
    
    :param state: Estado del inmueble para filtrar (pre_venta, en_venta, vendido).
    :param city: Ciudad del inmueble para filtrar.
    :param year_construction: Año de construcción del inmueble para filtrar.
    :return: Lista de diccionarios con la información de los inmuebles.
    :raises NoContentError: Si no se encuentran inmuebles con los filtros aplicados.
    """
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT p.address, p.city, s.name as status_name, p.price, 
                p.description                    
            FROM habi_db.property p
            INNER JOIN (
                SELECT property_id, MAX(update_date) as last_update
                FROM habi_db.status_history
                GROUP BY property_id
            ) sh ON p.id = sh.property_id
            INNER JOIN habi_db.status_history sh2 ON p.id = sh2.property_id AND sh.last_update = sh2.update_date
            INNER JOIN habi_db.status s ON sh2.status_id = s.id
            WHERE p.address != '' AND p.city != '' AND p.price != ''
            AND s.name IN ('pre_venta', 'en_venta', 'vendido')
        """

        params = []

        # Condiciones dinámicas basadas en los parámetros de entrada
        if state:
            query += " AND s.name = %s"
            params.append(state)
        if city:
            query += " AND p.city = %s"
            params.append(city)
        if year_construction:
            query += " AND REPLACE(CAST(p.year AS CHAR), '.', '') = %s"
            params.append(str(year_construction))
        print(query)
        cursor.execute(query, params)
        inmuebles = cursor.fetchall()
        
        if not inmuebles:
            raise NoContentError("No se encontraron inmuebles con los filtros aplicados.")
        
        return inmuebles
    finally:
        cursor.close()
        connection.close()
