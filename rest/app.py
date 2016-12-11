from flask import Flask, request
import os
import json

app = Flask(__name__)


@app.route("/datafiles", methods=["GET"])
def list_files():
    headers = {"Content-Type": "application/json"}
    data = os.listdir("datafiles")
    return json.dumps(data), 200, headers


@app.route("/datafiles/<filename>", methods=["GET"])
def get_file(filename):
    headers = {"Content-Type": "application/json"}
    data = {
        "filename": filename,
        "data": open(os.path.join("datafiles", filename)).read(),
    }
    return json.dumps(data), 200, headers


@app.route("/datafiles", methods=["POST"])
def create_file():
    new_file = json.loads(request.data)
    open(os.path.join("datafiles", new_file['filename']), "w").write(new_file['data'])
    return json.dumps(new_file), 201, {}


@app.route("/datafiles/<filename>", methods=["PUT"])
def update_file(filename):
    headers = {"Content-Type": "application/json"}
    update_file = json.loads(request.data)
    open(os.path.join("datafiles", filename), "w").write(update_file['data'])
    data = {
        "filename": filename,
        "data": update_file['data'],
    }
    return json.dumps(data), 200, headers


@app.route("/datafiles/<filename>", methods=["DELETE"])
def delete_file(filename):
    headers = {"Content-Type": "application/json"}
    os.unlink(os.path.join("datafiles", filename))
    return "", 204, {}

if __name__ == '__main__':
    app.run()
