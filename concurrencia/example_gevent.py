import gevent
from gevent import monkey; monkey.patch_all()
import urllib2
import os
from urls import *


def download_url_into_file(filename, url):
    response = urllib2.urlopen(url)
    fd = file(os.path.join("gevent", filename), "w")
    fd.write(response.read())
    fd.close()

jobs = []
for name, url in urls.items():
    filename = "%s.html" % name
    jobs.append(gevent.spawn(download_url_into_file, filename, url))

gevent.wait(jobs)

print "Finish!"
