from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime

with DAG(
    dag_id="run_php_kubernetes_pod",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    run_php = KubernetesPodOperator(
        task_id="run_php_script",
        name="php-runner",
        namespace="airflow",

        image="php:8.2-cli",
        cmds=["php"],
        arguments=["/scripts/my_job.php"],

        volumes=[
            {
                "name": "php-scripts",
                "configMap": {
                    "name": "php-scripts",
                },
            }
        ],
        volume_mounts=[
            {
                "name": "php-scripts",
                "mountPath": "/scripts",
                "readOnly": True,
            }
        ],

        is_delete_operator_pod=True,
        get_logs=True,
    )