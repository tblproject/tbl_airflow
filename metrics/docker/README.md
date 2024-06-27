# Notas 
El archivo **docker-compose.yml** incluye las siguientes configuraciones adicionales al archivo que se puede descargar para esta misma versión de Airflow (2.9.2) en la página oficial del proyecto:
- No incluye el despliegue de un servicio de PostgreSQL ya he utilizado una instancia de PostgreSQL 16 que tengo para varios labs.
- Incluye la configuración para habilitar Statsd en Airflow.
- Incluye el servicio statsd-exporter, que es el encargado de capturar las métricas de Airflow, aplicar el mapeo para traducirlas al formato esperaod por Prometheus y también es el servicio que recoge las peticiones de Prometheus para recuperar las métricas.