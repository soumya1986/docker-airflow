from airflow.plugins_manager import AirflowPlugin
from operators.DataTransferOperator import *
from sensors.filecount_sensor import FileCountSensor

class DemoPlugin(AirflowPlugin):

	name = 'demo_plugin'
	operators = [DataTransferOperator]
	sendors = [FileCountSensor]



