#DAG example to Lesson 2

from datetime import *

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import time as systemtime

args = {
    'owner': 'netology',
}

path = "/opt/airflow/dags"
filePath = path+"/test.txt"
bash_cmd = "ls " + path


def Counter(**context):
    ti = context["ti"]
    f = open(filePath, "r")
    counter = 0
    for x in f:
        print("Read line: ", x)
        counter = counter+1
    f.close()
    ti.xcom_push(key="file_count", value=counter)

    #print("counter=",counter)


def Worker():
    systemtime.sleep(5)
    print("Done!")


def PrintTask(**context):
    ti = context["ti"]
    var = ti.xcom_pull(task_ids="counter",key="file_count")
    print("counter=",var)


dag = DAG(dag_id='lesson2',default_args=args,start_date=datetime(2021,8,30))

task1 = BashOperator(dag=dag, bash_command=bash_cmd,task_id="check_files")


task2 = FileSensor(dag=dag,filepath=filePath,fs_conn_id="fs_connection",task_id="file_sensor",poke_interval=10)

task_counter = PythonOperator(dag=dag,task_id="counter", python_callable=Counter)

task_worker = PythonOperator(dag=dag,task_id="worker", python_callable=Worker)

task3 = PythonOperator(dag=dag,task_id="print_task", python_callable=PrintTask)

task1 >> task2 >> [task_counter,task_worker] >> task3