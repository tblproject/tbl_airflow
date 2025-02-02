# Configuración de integración con Marquez
Para integrar Airflow con Marquez, que implementa OpenLineage, son necesarios una serie de pasos, que se incluyen en este documento.

## Crear imagen custom
Es necesario instalar las librerías incluidas en **apache-airflow-providers-openlineage**, para ello se crea una imagen custom que instale esta dependencia.

Se incluye el archivo **Dockerfile** en el directorio **docker** para crearlo. Para crear la imagen se lanza:
```bash
docker build -t custom/airflow:2.10.4_ol .
```

Tras esto se debe modificar el archivo **docker-compose.yml** con el que se lanza Apache Airflow para que utilice esta nueva imagen custom. Para ello, paramos el servicio:
```bash
docker-compose down
```
Se modifica el archivo **docker-compose** para que utilice la image custom, cambiando la línea:
```yaml
image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.10.4}
```
Por la línea:
```yaml
image: ${AIRFLOW_IMAGE_NAME:-custom/airflow:2.10.4_ol}
```

## Configurar conexión a Marquez
Para esta conexión, en el archivo **docker-compose.yml** incorporaremos las siguientes variables de entorno, en donde se incorporarán las configuraciones de la conexión a nuestro servicio ded Marquez:
```yml

    # Marquez (OpenLineage) configs parameters:
    AIRFLOW__OPENLINEAGE__TRANSPORT: '{"type": "http", "url": "http://xxxx.xxx.xxx.xxx:5000", "endpoint": "api/v1/lineage"}'
    AIRFLOW__OPENLINEAGE__NAMESPACE: 'tbl-airflow-00'
    AIRFLOW__OPENLINEAGE__DISABLED: false
    AIRFLOW__OPENLINEAGE__DISABLE_SOURCE_CODE: true
```
En donde:
- **AIRFLOW__OPENLINEAGE__TRANSPORT**: se marca la configuración de la conexión en sí.
- **AIRFLOW__OPENLINEAGE__NAMESPACE**: se indica el namespace dentro de Marquez sobre el que escribirá los eventos.
- **AIRFLOW__OPENLINEAGE__DISABLED**: marcamos como habilitada la integración, esto lo incluyo por si en algún momento se quiere lanzar Airflow sin el registro de eventos de linaje, deshabilitarlo rápido.
- **AIRFLOW__OPENLINEAGE__DISABLE_SOURCE_CODE**: en algunos operadores como bashOperator y PythonOperator, dentro de la información del evento se incluye el código que ejecuta. Esta característica que viene aplciada por defecto, se puede inahbilitar con este parámetro, de esta forma evitamos que el código se lleve a los eventos de Marquez.