# Flask App: MP3 → MIDI via Transkun CLI

from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash
import os
import uuid
import subprocess

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, '..', 'templates')

# Use /tmp for ephemeral storage in serverless environments like Vercel
UPLOAD_FOLDER = os.path.join('/tmp', 'uploads')
OUTPUT_FOLDER = os.path.join('/tmp', 'outputs')
ALLOWED_EXTENSIONS = {'mp3'}

# Initialize app
app = Flask(__name__, template_folder=TEMPLATE_FOLDER)
app.secret_key = 'replace_with_random_secret'

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Check file extension

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            flash('Please select an MP3 file to upload.')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('Only .mp3 files are allowed.')
            return redirect(request.url)

        # Save upload with unique name
        uid = uuid.uuid4().hex
        in_name = f"{uid}.mp3"
        in_path = os.path.join(UPLOAD_FOLDER, in_name)
        file.save(in_path)

        # Transcribe: call Transkun CLI
        out_name = f"{uid}.mid"
        out_path = os.path.join(OUTPUT_FOLDER, out_name)
        cmd = ['transkun', in_path, out_path]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            flash('Transcription failed: ' + (result.stderr or 'Unknown error'))
            return redirect(request.url)

        return redirect(url_for('download_file', filename=out_name))

    return render_template('upload.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

# No need to run app here; Vercel invokes the Flask app directly

