import pytest
from unittest.mock import patch, MagicMock
from services.consulta_inmuebles_service import get_inmuebles

# Test sin filtros
@patch('db.db_connection.get_db_connection')
def test_get_inmuebles_no_filters(mock_db_conn):
    mock_cursor = MagicMock()
    mock_db_conn.return_value.cursor.return_value = mock_cursor
    result = get_inmuebles()
    assert len(result) > 0
    assert all(isinstance(inmueble, dict) for inmueble in result)

@patch('db.db_connection.get_db_connection')
def test_get_inmuebles_data_structure(mock_db_conn):
    mock_cursor = MagicMock()
    mock_db_conn.return_value.cursor.return_value = mock_cursor

    result = get_inmuebles()
    assert len(result) > 0  # Verifica que haya un resultado
    expected_keys = {"address", "city", "status_name", "price", "description"}
    # Verifica que cada inmueble tenga todas las claves esperadas
    for inmueble in result:
        assert set(inmueble.keys()) == expected_keys

# Test con filtro de estado
@patch('db.db_connection.get_db_connection')
def test_get_inmuebles_state_filter(mock_db_conn):
    mock_cursor = MagicMock()
    mock_db_conn.return_value.cursor.return_value = mock_cursor
    result = get_inmuebles(state='en_venta')
    for inmueble in result:
        assert inmueble['status_name'] == 'en_venta'


# Test con filtro de ciudad
@patch('db.db_connection.get_db_connection')
def test_get_inmuebles_city_filter(mock_db_conn):
    mock_cursor = MagicMock()
    mock_db_conn.return_value.cursor.return_value = mock_cursor
    result = get_inmuebles(city='bogota')
    for inmueble in result:
        assert inmueble['city'] == 'bogota'
    pass

# Test con filtro de año de construcción
@patch('db.db_connection.get_db_connection')
def test_get_inmuebles_year_construction_filter(mock_db_conn):
    mock_cursor = MagicMock()
    mock_db_conn.return_value.cursor.return_value = mock_cursor
    result = get_inmuebles(year_construction=2000)
    assert len(result) > 0

# Test con múltiples filtros
@patch('db.db_connection.get_db_connection')
def test_get_inmuebles_multiple_filters(mock_db_conn):
    mock_cursor = MagicMock()
    mock_db_conn.return_value.cursor.return_value = mock_cursor
    result = get_inmuebles(
        state='en_venta', city='bogota', year_construction=2011)
    for inmueble in result:
        assert inmueble['status_name'] == 'en_venta'
        assert inmueble['city'] == 'bogota'

# Test sin inmuebles encontrados (lanzando NoContentError)
@patch('db.db_connection.get_db_connection')
def test_get_inmuebles_no_content(mock_db_conn):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = []
    mock_db_conn.return_value.cursor.return_value = mock_cursor
    with pytest.raises(Exception):
        get_inmuebles(state='en_venta', city='bogota', year_construction=2000)

# Test con error en la consulta
@patch('db.db_connection.get_db_connection')
def test_get_inmuebles_query_error(mock_db_conn):
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = Exception('Error en la consulta')
    mock_db_conn.return_value.cursor.return_value = mock_cursor
    with pytest.raises(Exception):
        get_inmuebles(dia=2000)
