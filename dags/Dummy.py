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
	dag_id='dummy_operator',
	default_args=args,
	schedule_interval="@daily",
)

t0 = BashOperator(task_id='task_0', bash_command='echo "Hello World from Task 0"', dag=dag)
t1 = BashOperator(task_id='task_1', bash_command='echo "Hello World from Task 1"', dag=dag)
t2 = BashOperator(task_id='task_2', bash_command='echo "Hello World from Task 2"', dag=dag)
t3 = BashOperator(task_id='task_3', bash_command='echo "Hello World from Task 3"', dag=dag)
t4 = BashOperator(task_id='task_4', bash_command='echo "Hello World from Task 4"', dag=dag)
t5 = BashOperator(task_id='task_5', bash_command='echo "Hello World from Task 5"', dag=dag)
t6 = BashOperator(task_id='task_6', bash_command='echo "Hello World from Task 6"', dag=dag)
t7 = BashOperator(task_id='task_7', bash_command='echo "Hello World from Task 7"', dag=dag)
t8 = BashOperator(task_id='task_8', bash_command='echo "Hello World from Task 8"', dag=dag)
t9 = BashOperator(task_id='task_9', bash_command='echo "Hello World from Task 9"', dag=dag)
td = DummyOperator(task_id="dummy", dag=dag)

[t0,t1,t2,t3,t4] >> td >> [t5,t6,t7,t8,t9]
