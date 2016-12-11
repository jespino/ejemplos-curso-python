import threading
import urllib2
import os
from urls import *


def download_url_into_file(filename, url):
    response = urllib2.urlopen(url)
    fd = file(os.path.join("simple", filename), "w")
    fd.write(response.read())
    fd.close()

for name, url in urls.items():
    filename = "%s.html" % name
    download_url_into_file(filename, url)

print "Finish!"
