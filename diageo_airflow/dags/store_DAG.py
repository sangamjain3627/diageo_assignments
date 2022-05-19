from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.postgres_operator import PostgresOperator

from weather_data import weather_data_to_csv


default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2019, 12, 9),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

with DAG('store_dag',default_args=default_args,schedule_interval='@daily', template_searchpath=['/usr/local/airflow/sql_files'], catchup=False) as dag:

    t1 = PythonOperator(task_id='weather_data_csv_task', python_callable=weather_data_to_csv)

    t2 = PostgresOperator(task_id='create_postgres_table_task', postgres_conn_id="postgres_conn", sql="create_table.sql")

    t3 = PostgresOperator(task_id='insert_into_table_task', postgres_conn_id="postgres_conn", sql="insert_into_table.sql")

    t1 >> t2 >> t3
