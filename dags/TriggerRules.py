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
	dag_id='trigger_rules',
	default_args=args,
	schedule_interval="@daily",
)

t0 = BashOperator(task_id='task_0', bash_command='sleep 5', dag=dag)
t1 = BashOperator(task_id='task_1', bash_command='sleep 10', dag=dag)
t2 = BashOperator(task_id='task_2', bash_command='sleep 15', dag=dag)
t5 = BashOperator(task_id='task_5', bash_command='slp 15', dag=dag)
t7 = BashOperator(task_id='task_7', bash_command='slp 15', dag=dag)


t3 = BashOperator(task_id='task_3', bash_command='echo "Hello World from Task 3"', trigger_rule='one_success', dag=dag)
t4 = BashOperator(task_id='task_4', bash_command='echo "Hello World from Task 4"', trigger_rule='all_success', dag=dag)
t6 = BashOperator(task_id='task_6', bash_command='echo "Hello World from Task 5"', trigger_rule='all_done', dag=dag)
t8 = BashOperator(task_id='task_8', bash_command='echo "Hello World from Task 8"', trigger_rule='one_failed', dag=dag)
t9 = BashOperator(task_id='task_9', bash_command='echo "Hello World from Task 9"', trigger_rule='all_failed', dag=dag)
t10 = BashOperator(task_id='task_10', bash_command='echo "Hello World from Task 9"', trigger_rule='none_skipped', dag=dag)


[t0,t1,t2] >> t3

[t0,t1,t2] >> t4

[t0,t1,t2,t5] >> t6

[t0,t1,t2,t5] >> t8

[t5,t7] >> t9

[t0,t1,t2,t5,t7] >> t10

