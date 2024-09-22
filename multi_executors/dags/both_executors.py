from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    'test_both_executors',
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
        executor='LocalExecutor'
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
        executor='CeleryExecutor'
    )

    t1 >> t2
