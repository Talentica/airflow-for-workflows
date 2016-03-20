"""
Example with PythonOperator
"""
from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Samarth',
    'start_date': datetime(2016, 03, 15, 12),
}

# "schedule_interval" is your cron expression you can write any cron expression like unix cron.
dag = DAG('airflow_with_python_operator', default_args=default_args, schedule_interval="1 * * * *")

def my_function():
    '''This is a function that will run within the DAG execution'''
    return "Check me in the logs"

# Note that unlike other example we are using PythonOperator here.
# 'python_callable' parameter determines which python functions to 
# execute.
run_this = PythonOperator(
    task_id='run_my_function',
    python_callable=my_function,
    dag=dag)

