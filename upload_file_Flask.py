"""
@uthor : Gaurav Shrivastava
This code help the evidence collection app to upload the file through celery.
Particular this app help to from flask then another code will help to upload through the flask.
"""
from flask import Flask, jsonify
from celery import Celery
from flask import request
from new_celelry import upload_file 
import os

flask_app = Flask(__name__)

UPLOAD_FOLDER = r'C:\Users\Student\Desktop' # 
flask_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@flask_app.route("/", methods = ['Get', 'Post'])
def upload():
	file_ = request.files.getlist('upload')
	print(file_)
	name = []
	for file__ in file_:
		file_name = file__.filename
		file__.save(os.path.join(flask_app.config['UPLOAD_FOLDER'], file_name))
		print(name)
		upload_file.delay(filename = file_name)
	return "saved successfully"

if __name__ == "__main__":
	flask_app.run(debug = True)

