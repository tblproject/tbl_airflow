from airflow import DAG, Dataset
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.lineage.entities import Table, File

import pandas as pd
import os

# Define dataset as a local file
CSV_DATASET_PATH = "/opt/airflow/dags/data/query_result.csv"
CSV_DATASET_URI = f"file://{CSV_DATASET_PATH}"
csv_dataset = File(url = CSV_DATASET_URI)


def save_to_csv(query_result, file_path):
    """Save query result to a CSV file."""
    df = pd.DataFrame(query_result)
    df.to_csv(file_path, index=False)

def process_csv(file_path):
    """Process the CSV file and register lineage dataset."""
    print(f"Processing dataset from {file_path}")
    

with DAG(
    dag_id="test_data_lineage",
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    tags=["elt", "sql", "csv"],
):
    
    extract_query = SQLExecuteQueryOperator(
        task_id="extract_query",
        conn_id="tbl_project_marquez_id",
        sql="SELECT * FROM public.jobs LIMIT 100;",
        return_last=True,  # Ensure the last query's result is returned
    )
    
    save_csv_task = PythonOperator(
       task_id="save_csv",
       python_callable=save_to_csv,
       op_kwargs={
            "query_result": extract_query.output,
            "file_path": CSV_DATASET_PATH
        },
        outlets=[csv_dataset],  # Registering dataset output
    )
    
    process_csv_task = PythonOperator(
        task_id="process_csv",
        python_callable=process_csv,
        op_kwargs={"file_path": CSV_DATASET_PATH},
        inlets=[csv_dataset]
    ) 
    
    extract_query >> save_csv_task >> process_csv_task
