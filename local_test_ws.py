from flask import Flask, send_from_directory

app = Flask(__name__)

@app.get("/<file_name>")
def get_css_file(file_name):
    return send_from_directory("./", path=f"{file_name}")

app.run(host="localhost", port=80)