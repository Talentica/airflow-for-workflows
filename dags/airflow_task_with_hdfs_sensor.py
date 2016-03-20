"""
Executing tasks when particular hdfs file is uploaded/appeared to hdfs
"""
from airflow import DAG
from airflow.operators import BashOperator, HdfsSensor
from datetime import datetime, timedelta, time


default_args = {
    'owner': 'Samarth',
    'start_date': datetime(2016, 03, 15, 12),
}

# "schedule_interval" is your cron expression you can write any cron expression like unix cron.
dag = DAG('airflow_task_with_hdfs_sensor', default_args=default_args, schedule_interval="1 * * * *")

bash_task = BashOperator(
    task_id='dependency_for_hdfs_sensor',
    bash_command='echo "HDFS sensor would only be enabled after I am done!"',
    dag=dag)

# Sensor operator takes "filepath" to check if this file is present in hdfs or not.
# "hdfs_conn_id" is configured in ui Admin--> Connection.
hdfs_sensor_task = HdfsSensor(
    task_id='hdfs_sensor_task',
    filepath='/user/samarthg/input2',
    hdfs_conn_id='webhdfs_default',
    dag=dag)

post_hdfs_sensor_task = BashOperator(
    task_id='post_hdfs_sensor_task',
    bash_command='echo "I am done, it means sensor has done its job."',
    dag=dag)

# Setting up the correct dependencies for defined tasks.
hdfs_sensor_task.set_upstream(bash_task)
post_hdfs_sensor_task.set_upstream(hdfs_sensor_task)
