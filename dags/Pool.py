import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators import BashOperator
from airflow.operators.dummy_operator import DummyOperator

args = {
	'owner': 'Airflow',
	'start_date': airflow.utils.dates.days_ago(1),
}


dag = DAG(
	dag_id='pools',
	default_args=args,
	schedule_interval="@daily",
)


t1 = BashOperator(task_id='task_1', bash_command='echo "Hello World from Task 1"', dag=dag, pool = 'pool_1', priority_weight = 1)
t2 = BashOperator(task_id='task_2', bash_command='echo "Hello World from Task 2"', dag=dag, pool = 'pool_1', priority_weight = 2)
t3 = BashOperator(task_id='task_3', bash_command='echo "Hello World from Task 3"', dag=dag, pool = 'pool_2', priority_weight = 3)
t4 = BashOperator(task_id='task_4', bash_command='echo "Hello World from Task 4"', dag=dag, pool = 'pool_2', priority_weight = 4)

