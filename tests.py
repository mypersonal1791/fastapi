import requests


def call_upload_pdf(path):
    url = "https://upload-portal.onrender.com/upload"  # replace with your Flask app's URL



    with open(path, "rb") as f:
        response = requests.post(url, files={"file": f})
    print(response.status_code)
    print(response.text)
    return response


resp = call_upload_pdf(path)
print(resp)