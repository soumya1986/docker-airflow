import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from random import randint


args = {
	'owner': 'Airflow',
	'start_date': airflow.utils.dates.days_ago(1),
}


dag = DAG(
	dag_id='branch_operation',
	default_args=args,
	schedule_interval="@daily",
)


def generate_number(**kwargs):
	value = randint(0, 10)
	return value

def branch_function(**kwargs):
	ti = kwargs['ti']
	pulled_number = ti.xcom_pull()
	if(pulled_number%2 == 0):
		return 'even_task'
	else:
		return 'odd_task'


t1 = PythonOperator(task_id='generate_number', python_callable=generate_number, provide_context=True, dag=dag)
t2 = BranchPythonOperator(task_id="branch_task", python_callable=branch_function, provide_context=True, dag=dag)
t3 = BashOperator(task_id='even_task', bash_command='echo "Got even value"', dag=dag)
t4 = BashOperator(task_id='odd_task', bash_command='echo "Got odd value"', dag=dag)


t1 >> t2 >> [t3,t4]



