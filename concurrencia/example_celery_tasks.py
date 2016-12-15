from celery import Celery
import urllib2
import os

app = Celery('tasks', broker='redis://localhost', backend="redis://localhost")

@app.task
def download_url_into_file(filename, url):
    response = urllib2.urlopen(url)
    fd = file(os.path.join("celery", filename), "w")
    fd.write(response.read())
    fd.close()
