# dags/example_k8s_dag.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

# Pfad zu deinen Scripts
sys.path.append("/opt/airflow/scripts")

from helper import hello

with DAG(
    dag_id="example_k8s_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # manuell triggern
    catchup=False,
    tags=["example"],
) as dag:

    run_hello = PythonOperator(
        task_id="run_hello",
        python_callable=hello
    )