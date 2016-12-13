from flask import Flask, render_template
import json
import datetime

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
    return value.strftime("%A %d. %B %Y")

@app.route("/logs")
def index():
    logs = [
        LogEntry(datetime.datetime.now(), ERROR, "Error logged"),
        LogEntry(datetime.datetime.now(), WARN, "Warning logged"),
        LogEntry(datetime.datetime.now(), INFO, "Info logged"),
    ]

    return render_template("logs.jinja", logs=logs)

if __name__ == "__main__":
    app.run()
