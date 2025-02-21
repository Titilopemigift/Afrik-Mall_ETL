from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Default settings for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 19),  
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'afrik_mall_etl',  # Name of the DAG
    default_args=default_args,
    description='ETL pipeline for Afrik Mall sales data',
    schedule_interval='@daily',  # Run daily
)

# Define the ETL task
def run_etl():
    subprocess.run(["python3", "c:Users/TITILOPE/airflow/dags/etl_pipeline.py"]) 

run_etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag,
)

run_etl_task
