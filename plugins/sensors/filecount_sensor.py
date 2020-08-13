from airflow.operators.sensors import BaseSensorOperator
from airflow.contrib.hooks.fs_hook import FSHook
from airflow.utils.decorators import apply_defaults
import os, stat

class FileCountSensor(BaseSensorOperator):

	@apply_defaults
	def __init__(self, dir_path, conn_id, *args, **kwargs):
		
		self.dir_path = dir_path
		self.conn_id = conn_id
		super().__init__(*args, **kwargs)

	def poke(self, context):

		hook = FSHook(self.conn_id)
		base_path = hook.get_path()
		full_path = os.path.join(base_path, self.dir_path)
		try:
			for root, dirs, files in os.walk(full_path):
				if len(files) >= 5:
					return True
		except OSError:
			return False
		return False