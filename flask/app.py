from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.jinja")

@app.route("/stats")
def stats():
    data = json.load(open("stats.json"))
    return render_template("stats.jinja", **data)

if __name__ == "__main__":
    app.run()
