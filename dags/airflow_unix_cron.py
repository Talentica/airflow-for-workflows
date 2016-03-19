"""
Trying to create a simple cron like behaviour with airflow dag
"""
from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Samarth',
    'start_date': datetime(2016, 03, 15, 12),
}

# "schedule_interval" is your cron expression you can write any cron expression like unix cron.
dag = DAG('airflow_unix_cron', default_args=default_args, schedule_interval="20,21,23 * * * *")

# This is the task which executes your command as per the dag scheduled.
# "bash_command" is the parameter where you provide your command to be executed.
task1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

