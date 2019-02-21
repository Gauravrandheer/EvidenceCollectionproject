"""
@uthor : Gaurav Shrivastava
this code help our app to upload file asynchronously so that a user does not need to wait for uploading inorder to use more functionality of out app.
Particularly this code will run after flask upload and upload this to the server.
"""

from flask import Flask
from celery import Celery
from flask import request

celery = Celery('flask-celery-inherited', broker = 'redis://localhost:6379', backend = 'redis://localhost:6379')

@celery.task
def upload_file(filename):
	path = r'C:\Users\Student\Desktop/'+ str(filename)
	with open(path, 'rb') as file:
		data = file.read()

	with open(filename, 'wb') as f:
		f.write(data)

	file.close()
	f.close()
