from airflow import DAG
from datetime import datetime, timedelta
from operators.DataTransferOperator import DataTransferOperator
from sensors.filecount_sensor import FileCountSensor
#from operators.DataTransferOperator import DataTransferOperator


dag = DAG("plugins_dag", schedule_interval=timedelta(1), start_date=datetime(2020, 8, 11), catchup=False)

t1 = DataTransferOperator(

	task_id = 'data_transfer',
	source_file_path = '/usr/local/airflow/plugins/data/source.txt',
	dest_file_path = '/usr/local/airflow/plugins/data/destination.txt',
	delete_list = ['Airflow', 'is'],
	dag = dag

)

t2 = FileCountSensor(

	task_id = 'file_count_sensor',
	dir_path = '/usr/local/airflow/plugins/data',
	conn_id = 'fs_default',
	poke_interval = 5,
	timeout = 15,
	dag = dag

)
