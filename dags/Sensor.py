import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.sensors.file_sensor import FileSensor


args = {
	'owner': 'Airflow',
	'start_date': airflow.utils.dates.days_ago(1),
}


dag = DAG(
	dag_id='sensor_operator',
	default_args=args,
	schedule_interval="@daily",
)


fl = FileSensor(
	task_id='file_check',
	filepath='/usr/local/airflow/test.txt',
	fs_conn_id='fs_default',
	poke_intervel=5,
	timeout=60,
	soft_fail=True,
	dag=dag
)

t1 = BashOperator(task_id='task_0', bash_command='cat /usr/local/airflow/test.txt', dag=dag)

fl >> t1



