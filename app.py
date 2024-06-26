
from flask import Flask, request
import shutil
import os
import supabase

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_pdf():
    # check if the post request has the file part
    if 'file' not in request.files:
        return {"detail": "No file part in request."}, 400

    file = request.files['file']

    # if no file is selected
    if file.filename == '':
        return {"detail": "No selected file."}, 400

    if not file.filename.endswith(".pdf") and not file.filename.endswith(".png") and not file.filename.endswith(".jpg"):
        return {"detail": "Invalid file type. PDF file expected."}, 400

    if file:
        filename = file.filename
        #file_path = os.path.join(os.getcwd(), filename)
        from supabase import create_client, Client

        url: str = 'https://hdgdccrpmfbjcxjuzlct.supabase.co'
        key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhkZ2RjY3JwbWZiamN4anV6bGN0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxMzA0MDg2OSwiZXhwIjoyMDI4NjE2ODY5fQ.8SlQy0zWReo0__PJHt1mInNtNNtIzOeZs2kiEPXAADE'
        supabase: Client = create_client(url, key)
        bucket_name: str = "Images"
        contents = file.read()
        path = 'Work/' + file.filename
        try:

            data = supabase.storage.from_(bucket_name).upload('Work/' + file.filename, contents)

            res = supabase.storage.from_(bucket_name).get_public_url(path)
        except:
            res = supabase.storage.from_(bucket_name).get_public_url(path)

        return {"file url": f"{res}", "message": "File saved locally."}, 200


@app.route('/')
def hello_world():
    return 'Hello, World!'