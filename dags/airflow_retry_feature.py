"""
To make the task retry on failure
"""
from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

# 'retries' options make sure every failed tasks is attempted twice.
# 'retry_delay' provides the delay between the attempts. If task did not
# succeeds in given number of retries then airflow marks it as failed.
default_args = {
    'owner': 'Samarth',
    'start_date': datetime(2016, 03, 19, 6),
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG('airflow_unix_cron', default_args=default_args, schedule_interval="0 * * * *")

# For the sake of experimenting with retries you can provide any wrong command
# below. Once the command fails executing it is ready for re-execution after 2
# minutes of delay. You can check it in airflow ui
taks_to_fail = BashOperator(
    task_id='fail_and_retry',
    bash_command='sl',
    dag=dag)

