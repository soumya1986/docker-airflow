from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataTransferOperator(BaseOperator):

	@apply_defaults
	def __init__(self, source_file_path, dest_file_path, delete_list, *args, **kwargs):

		self.source_file_path = source_file_path
		self.dest_file_path = dest_file_path
		self.delete_list = delete_list
		super().__init__(*args, **kwargs)

	def execute(self, context):

		fin = open(self.source_file_path)
		fout = open(self.dest_file_path,'w')

		for line in fin:
			for word in self.delete_list:
				line = line.replace(word, "")
			fout.write(line)

		fin.close
		fout.close
