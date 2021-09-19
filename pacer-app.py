import os
from flask import Flask
from flask import request

app = Flask(__name__)

def check_tmp():
    if not os.path.exists('tmp'):
        os.makedirs('tmp')

@app.route('/info', methods=['GET'])
def info():
    return {
        "status_message": "Info ok",
        "status_code": 0
    }

@app.route('/upload-reference', methods=['POST'])
def upload_reference():
    check_tmp()
    f = request.files['reference_file']
    f.save('./tmp/reference_file.gpx')
    return {
        "filename": "tmp/reference_file.gpx",
        "status_message": "Upload successful",
        "status_code": 0
    }
