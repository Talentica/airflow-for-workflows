"""
Trying to create a simple cron like behaviour with airflow dag
"""
from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Samarth',
    'depends_on_past': False,
    'email': ['samarth.gahire@talentica.com'],
    'start_date': datetime(2016, 03, 15, 12),
    'email_on_failure': False,
}

dag = DAG('airflow_unix_cron', default_args=default_args, schedule_interval="20,21,23 * * * *")

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

t1.doc_md = """
#### Task Documentation
"""
