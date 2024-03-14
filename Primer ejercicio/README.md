# Microservicios de Consulta y "Me Gusta" para Inmuebles

Este repositorio contiene la implementación de dos microservicios solicitados por Habi: uno para consultar inmuebles disponibles y otro para la funcionalidad de "Me Gusta".

## Tecnologías Utilizadas

- Python (Versión 3.12.0)
- colorama==0.4.6
- coverage==7.4.3
- iniconfig==2.0.0
- mock==5.1.0
- mysql-connector-python==8.3.0
- packaging==24.0
- pluggy==1.4.0
- pytest==8.1.1
- pytest-cov==4.1.0
- python-dotenv==1.0.1

## Desarrollo del Microservicio de Consulta

### Funcionalidades Implementadas

- Consulta de inmuebles disponibles según filtros especificados por el usuario.
- Filtros disponibles: Año de construcción, Ciudad, Estado.
- Visualización de la información del inmueble: Dirección, Ciudad, Estado, Precio de venta, Descripción.
- Estado actual del inmueble determinado por el último estado insertado en la tabla "status_history".

### Endpoints y Métodos Admitidos

- `/inmuebles`
  - Método: GET
  - Parámetros:
    - `state` (opcional): Estado del inmueble (pre_venta, en_venta, vendido)
    - `city` (opcional): Ciudad del inmueble
    - `year_construction` (opcional): Año de construcción del inmueble

### Estructura del Proyecto

El código del microservicio de consulta está organizado de la siguiente manera:

- `server.py`: Punto de entrada del microservicio.
- `db/db_connection.py`: Funciones para interactuar con la base de datos MySQL.
- `services/consulta_inmuebles_service.py`: Funciones para aplicar los filtros de consulta.
- `utils/`: Directorio de funciones de utilidad.
- `tests/`: Directorio que contiene las pruebas unitarias.
- `handler/`: Directorio de maneja las solicitudes HTTP.

## Desarrollo del Microservicio de "Me Gusta" (No implementado)

### Extensión del Modelo de la Base de Datos

Se ha extendido el modelo de la base de datos para incluir la funcionalidad de "Me Gusta". A continuación, se presenta el diagrama de Entidad-Relación (ER) propuesto y el código SQL correspondiente:

#### Diagrama de Entidad-Relación (ER)

![Diagrama de Entidad-Relación (ER)](https://github.com/Danielmc09/pruebaHABI/blob/main/Primer%20ejercicio/img/esquema_full.png)

#### Código SQL para la Extensión del Modelo

```sql
CREATE TABLE property_like (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    property_id INT,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (property_id) REFERENCES Properties(property_id)
);
```

## Ejecución del Proyecto

Para ejecutar el microservicio de consulta, sigue estos pasos:

1. Instala las dependencias utilizando `pip install -r requirements.txt`.
2. Configura las credenciales de la base de datos en el archivo `.env`.
3. Ejecuta `python server.py` para iniciar el servidor.

# Recomendaciones

- se recomienda crear un entorno virtual para este proyecto, con el fin de que no genere conflicto con otras librerias 

## Pruebas Unitarias

El código del microservicio de consulta incluye pruebas unitarias para garantizar su correcto funcionamiento. Para ejecutar las pruebas, utiliza el comando `pytest`.

---

Recuerda que este README es una guía inicial y puede ser modificado y extendido según sea necesario a lo largo del desarrollo del proyecto.
