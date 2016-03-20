"""
Multiple tasks in a dag with dependencies.
"""
from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Samarth',
    'start_date': datetime(2016, 03, 15, 12),
}

# "schedule_interval" is your cron expression you can write any cron expression like unix cron.
dag = DAG('airflow_dependency_feature', default_args=default_args, schedule_interval="1 * * * *")

task1 = BashOperator(
    task_id='first_task_in_dependency',
    bash_command='echo "I am the first task"',
    dag=dag)

task2 = BashOperator(
    task_id='dependant_task',
    bash_command='echo "I am dependent task"',
    dag=dag)

# This will make sure that the task2 is executed only after task1 is executed.
task2.set_upstream(task1)
