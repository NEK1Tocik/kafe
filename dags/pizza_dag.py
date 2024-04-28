import datetime
import time
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


pizza_dag = DAG("pizza_dag", start_date=datetime.datetime.now())

task1 = BashOperator(task_id='print_directories', bash_command='ls -la', dag=pizza_dag)
task2 = BashOperator(task_id='sleep', bash_command='sleep 5', dag=pizza_dag)
task3 = BashOperator(task_id='print_date', bash_command='date', dag=pizza_dag)


def cook_pizza():
    pass


task4 = PythonOperator(task_id='make_pizza', python_callable=cook_pizza, dag=pizza_dag)

task1 >> task2 >> task3 >> task4
