from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    'test_celery_executor',
    default_args={"executor": "CeleryExecutor"},  # Applies to all tasks in the DAG
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t1 >> t2
