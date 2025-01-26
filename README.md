# Contenido del repositorio

- **metrics**: archivos utilizados para configurar el envío de métricas a Prometheus, para explotarlas desde Grafana. Las métricas son generadas a través del servicio Statsd que ofrece Airflow dentro de las opciones de configuración para la generación y envío de métricas.
    - **mapping**: contiene un archivo de mapeo entre las métricas que genera Statsd y el formato de Prometheus. 
    - **prometheus**: contiene un archivo de configuración base de Prometheus.
- **multi_executors**: incluye varios dags de ejemplo para la entrada en donde se explica cómo configurar múltiples executors en Airflow.
- **data_lineage**: se incluyen archivos y dags utilizados para integrar Airflow con una plataforma como Marquez que implementa OpenLineage para el Linaje de Datos.