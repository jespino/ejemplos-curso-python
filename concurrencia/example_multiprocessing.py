import multiprocessing
import urllib2
import os
from urls import *


def download_url_into_file(filename, url):
    response = urllib2.urlopen(url)
    fd = file(os.path.join("multiprocessing", filename), "w")
    fd.write(response.read())
    fd.close()

procs = []
for name, url in urls.items():
    filename = "%s.html" % name
    proc = multiprocessing.Process(target=download_url_into_file, args=[filename, url])
    proc.start()
    procs.append(proc)

for proc in procs:
    proc.join()

print "Finish!"
