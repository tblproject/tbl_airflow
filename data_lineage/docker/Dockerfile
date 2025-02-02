FROM apache/airflow:2.10.4
USER root
RUN apt update; apt upgrade -y
RUN pip3 install apache-airflow-providers-openlineage==2.0.0
USER airflow 