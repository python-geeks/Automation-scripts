# External Imports
import os
from flask import render_template, request, send_file

# Internal Imports
from app import app
from app.utils import generate_certificate


@app.after_request
def add_header(r):
    """
    Prevents caching, which will make sure old files are not sent.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/', methods=['GET', 'POST'])
def home():
    '''home
    Renders home page
    '''
    return render_template("certificate.html")


@app.route('/render', methods=['POST'])
def render_certificate():
    """
    Get's information from user and generates
    the certificate using generate_certificate function
    """
    if request.method == "POST":
        file_name = generate_certificate(
            request.form['name'],
            request.form['pr_num'])
        return render_template('download.html', file_name=file_name)


@app.route('/download_certificate', methods=['GET'])
def download():
    """
    Download the generated certificate
    """
    if request.method == "GET":
        filename = request.args.get("filename")
        filepath = os.path.join("static/certificates/generated", filename)
        return send_file(filepath, as_attachment=True, cache_timeout=0,
                         attachment_filename=filename)
