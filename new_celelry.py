from flask import Flask
from celery import Celery
from flask import request

celery = Celery('flask-celery-inherited', broker = 'redis://localhost:6379', backend = 'redis://localhost:6379')

@celery.task
def upload_file(filename):

	# filename = str(filename)
	print(filename)
# for files in filename:
	path = r'C:\Users\Student\Desktop/'+ str(filename)

	with open(path, 'rb') as file:
		data = file.read()

	with open(filename, 'wb') as f:
		f.write(data)

	file.close()
	f.close()
