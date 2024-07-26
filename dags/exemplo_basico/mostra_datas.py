from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "mostra_datas",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2024, 7, 18),
    catchup=True,
    tags=["mostra_datas"],
) as dag:

    t1 = BashOperator(
        task_id="print_date",
        bash_command="echo 'Data definida na operacao: {{ds}}'",
    )

    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )

    t3 = BashOperator(
        task_id="print_real_date",
        depends_on_past=False,
        bash_command="date -I",
    )

    t1 >> [t2,t3]