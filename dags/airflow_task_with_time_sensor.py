"""
Executing tasks at a particular time of the day using sensor operator.
"""
from airflow import DAG
from airflow.operators import BashOperator, TimeSensor
from datetime import datetime, timedelta, time


default_args = {
    'owner': 'Samarth',
    'start_date': datetime(2016, 03, 15, 12),
}

# "schedule_interval" is your cron expression you can write any cron expression like unix cron.
dag = DAG('airflow_task_with_time_sensor', default_args=default_args, schedule_interval="1 * * * *")

bash_task = BashOperator(
    task_id='dependency_for_sensor',
    bash_command='echo "Sensor would only be enabled after I am done!"',
    dag=dag)

# Sensor operator takes "target_time" which is a specific time in a day irrespective of date/day.
# Sensor is executed once the target time has passed. In this case after 10:55 at morning.
sensor_task = TimeSensor(
    task_id='sensor_task',
    target_time=time(10,55,1,1),
    dag=dag)

post_sensor_task = BashOperator(
    task_id='post_sensor_task',
    bash_command='echo "I am done, it means sensor has done its job."',
    dag=dag)

# Setting up the correct dependencies for defined tasks.
sensor_task.set_upstream(bash_task)
post_sensor_task.set_upstream(sensor_task)
