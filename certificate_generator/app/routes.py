from app import app
from app.utils import generate_certificate
from flask import render_template, request, send_file
import os

@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template("certificate.html")


@app.route('/download', methods=['GET', 'POST'])
def download_certificate():
    if request.method == "POST":
        file_name = generate_certificate(request.form['name'])
        return render_template('download.html', file_name=file_name)

@app.route('/download_certificate', methods=['GET'])
def method_name():
    if request.method == "GET":
        filename = request.args.get("filename")
        filepath = os.path.join("static/certificates/generated", filename)
        return send_file(filepath, as_attachment=True, cache_timeout=0, attachment_filename=filename)
