from app import app
from app.utils import generate_certificate
from flask import render_template, request, send_file
import os


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template("certificate.html")


@app.route('/render', methods=['POST'])
def render_certificate():
    if request.method == "POST":
        file_name = generate_certificate(request.form['name'], request.form['pr_num'])
        return render_template('download.html', file_name=file_name)

@app.route('/download_certificate', methods=['GET'])
def download():
    if request.method == "GET":
        filename = request.args.get("filename")
        filepath = os.path.join("static/certificates/generated", filename)
        return send_file(filepath, as_attachment=True, cache_timeout=0, attachment_filename=filename)
