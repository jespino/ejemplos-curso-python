from flask import Flask, render_template
import json
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

@app.route("/logs")
def index():
    conn = sqlite3.connect(app.config['DBFILE'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs")
    logs = [LogEntry(log[0], log[1], log[2]) for log in cur.fetchall()]
    return Ok(render_template("logs.jinja", logs=logs))

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
    cur.execute("INSERT INTO logs VALUES(?, ?, ?)", (datetime.datetime.now(), level, message))
    conn.commit()
    conn.close()

@cli.command()
def initdb():
    conn = sqlite3.connect(app.config['DBFILE'])
    cur = conn.cursor()
    cur.execute("CREATE TABLE logs (datetime DATETIME, level INT, message VARCHAR)")
    conn.commit()
    conn.close

if __name__ == "__main__":
    cli()
