import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators import BashOperator
from airflow.operators.subdag_operator import SubDagOperator
from subdags.SubDagChild import subdag

DAG_ID = 'SubDagParent'
SUB_DAG_ID = "section_subdag"

args = {
	'owner': 'Airflow',
	'start_date': airflow.utils.dates.days_ago(1),
}


dag = DAG(
	dag_id=DAG_ID,
	default_args=args,
	schedule_interval="@daily",
)

start = BashOperator(task_id='start', bash_command='echo "Hello World from Task Start"', dag=dag)

section_subdag = SubDagOperator(
	task_id="section_subdag",
	subdag=subdag(DAG_ID,SUB_DAG_ID,args),
	dag=dag)

end = BashOperator(task_id='end', bash_command='echo "Hello World from Task End"', dag=dag)

start >> section_subdag >> end