import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators import BashOperator


args = {
	'owner': 'Airflow',
	'start_date': airflow.utils.dates.days_ago(1),
}

def subdag(parent_dag_id, child_dag_id, args):

	sub_dag = DAG(
		dag_id='%s.%s' % (parent_dag_id, child_dag_id),
		default_args=args,
		schedule_interval="@daily",
	)

	t0 = BashOperator(task_id='task_0', bash_command='echo "Hello World from Task 0"', dag=sub_dag)
	t1 = BashOperator(task_id='task_1', bash_command='echo "Hello World from Task 1"', dag=sub_dag)
	t2 = BashOperator(task_id='task_2', bash_command='echo "Hello World from Task 2"', dag=sub_dag)
	t3 = BashOperator(task_id='task_3', bash_command='echo "Hello World from Task 3"', dag=sub_dag)
	t4 = BashOperator(task_id='task_4', bash_command='echo "Hello World from Task 4"', dag=sub_dag)

	return sub_dag


