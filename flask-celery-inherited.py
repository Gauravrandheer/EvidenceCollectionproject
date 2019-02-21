from flask import Flask, jsonify
from celery import Celery
from flask import request
from new_celelry import upload_file 
import os

fl = Flask(__name__)

UPLOAD_FOLDER = r'C:\Users\Student\Desktop'
fl.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@fl.route("/", methods = ['Get', 'Post'])
def upload():

	# file__ = request.files['upload']
	# file_ = request.files.getlist(["upload"])
	# file_ = request.files.to_dict()
	file_ = request.files.getlist('upload')
	print(file_)
	name = []
	for file__ in file_:
		file_name = file__.filename
		file__.save(os.path.join(fl.config['UPLOAD_FOLDER'], file_name))
		# name.append(file_name)
		print(name)
		upload_file.delay(filename = file_name)
	return "saved successfully"
if __name__ == "__main__":
	fl.run(debug = True)

if __name__ == "__main__":
	fl.run(debug = True)
