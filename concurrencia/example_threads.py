import threading
import urllib2
import os
from urls import *


def download_url_into_file(filename, url):
    response = urllib2.urlopen(url)
    fd = file(os.path.join("threads", filename), "w")
    fd.write(response.read())
    fd.close()

threads = []
for name, url in urls.items():
    filename = "%s.html" % name
    thread = threading.Thread(target=download_url_into_file, args=[filename, url])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print "Finish!"
