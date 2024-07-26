from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
  print('Hello World!')

with DAG(
  dag_id="dag_hello_world",
  catchup=False
) as dag:
  
  hello_world_task = PythonOperator(
    task_id="hello_world",
    python_callable=hello_world
  )

hello_world_task