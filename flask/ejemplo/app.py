from flask import Flask, render_template, request
import json
import re
import datetime
from responses import *
import click
import sqlite3

ERROR = 1
WARN = 2
INFO = 3

class LogEntry(object):
    def __init__(self, datetime, level, message):
        self.datetime = datetime
        self.level = level
        self.message = message

    def level_name(self):
        if self.level == 1:
            return "ERROR"
        elif self.level == 2:
            return "WARN"
        return "INFO"

app = Flask(__name__)
app.config.from_pyfile("config.cfg")

@app.template_filter('datetime')
def format_datetime(value):
    return value

@app.route("/logs", methods=["GET"])
def list_logs():
    headers = {"Content-Type": "application/json"}
    conn = sqlite3.connect(app.config['DBFILE'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs")
    logs = [{"id": log[0], "datetime": log[1], "level": log[2], "message": log[3]} for log in cur.fetchall()]
    conn.commit()
    conn.close()

    filter_query = request.args.get('filter', None)
    if filter_query:
        pattern = re.compile(filter_query)
        filtered_logs = []
        for log in logs:
            if re.match(pattern, log['message']):
                filtered_logs.append(log)
        logs = filtered_logs

    return json.dumps(logs), 200, headers

@app.route("/logs/<int:log_id>", methods=["GET"])
def get_log(log_id):
    headers = {"Content-Type": "application/json"}
    conn = sqlite3.connect(app.config['DBFILE'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs WHERE id=?", (log_id,))
    log = cur.fetchone()
    log = {"id": log[0], "datetime": log[1], "level": log[2], "message": log[3]}
    conn.commit()
    conn.close()
    return json.dumps(log), 200, headers

@app.route("/logs/<int:log_id>", methods=["DELETE"])
def delete_log(log_id):
    headers = {"Content-Type": "application/json"}
    conn = sqlite3.connect(app.config['DBFILE'])
    cur = conn.cursor()
    cur.execute("DELETE FROM logs WHERE id=?", (log_id,))
    conn.commit()
    conn.close()
    return "", 204, headers

@app.route("/logs/<int:log_id>", methods=["PUT"])
def update_log(log_id):
    headers = {"Content-Type": "application/json"}
    log_data = json.loads(request.data)
    conn = sqlite3.connect(app.config['DBFILE'])
    cur = conn.cursor()
    cur.execute("UPDATE logs SET datetime=?, level=?, message=? where id=?", (log_data['datetime'], log_data['level'], log_data['message'], log_id))
    conn.commit()
    cur.execute("SELECT * FROM logs WHERE id=?", (log_id,))
    log = cur.fetchone()
    log = {"id": log[0], "datetime": log[1], "level": log[2], "message": log[3]}
    conn.commit()
    conn.close()
    return json.dumps(log), 200, headers

@app.route("/logs", methods=["POST"])
def new_log_entry():
    headers = {"Content-Type": "application/json"}
    log_data = json.loads(request.data)
    conn = sqlite3.connect(app.config['DBFILE'])
    cur = conn.cursor()
    cur.execute("INSERT INTO logs VALUES(NULL, ?, ?, ?)", (log_data['datetime'], log_data['level'], log_data['message']))
    conn.commit()
    cur.execute("SELECT * FROM logs WHERE id=?", (cur.lastrowid,))
    log = cur.fetchone()
    log = {"id": log[0], "datetime": log[1], "level": log[2], "message": log[3]}
    conn.commit()
    conn.close()
    return json.dumps(log), 201, headers

@click.group()
def cli():
    pass

@cli.command()
@click.option("-p", "--port", default=5000)
def run(port):
    app.run(port=port)

@cli.command()
@click.option("-l", "--level", type=click.Choice(["ERROR","WARN","INFO"]), default="INFO")
@click.argument("message")
def add_log_entry(level, message):
    if level == "ERROR":
        level = 1
    elif level == "WARN":
        level = 2
    elif level == "INFO":
        level = 3
    conn = sqlite3.connect(app.config['DBFILE'])
    cur = conn.cursor()
    cur.execute("INSERT INTO logs VALUES(NULL, ?, ?, ?)", (datetime.datetime.now(), level, message))
    conn.commit()
    conn.close()

@cli.command()
def initdb():
    conn = sqlite3.connect(app.config['DBFILE'])
    cur = conn.cursor()
    cur.execute("CREATE TABLE logs (id INTEGER PRIMARY KEY AUTOINCREMENT, datetime DATETIME, level INT, message VARCHAR)")
    conn.commit()
    conn.close

if __name__ == "__main__":
    cli()
