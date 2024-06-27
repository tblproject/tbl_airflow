# Contenido del repositorio

- **metrics**: archivos utilizados para configurar el envío de métricas a Prometheus, para explotarlas desde Grafana. Las métricas son generadas a través del servicio Statsd que ofrece Airflow dentro de las opciones de configuración para la generación y envío de métricas.
    - **mapping**: contiene un archivo de mapeo entre las métricas que genera Statsd y el formato de Prometheus. 
    - **prometheus**: contiene un archivo de configuración base de Prometheus.