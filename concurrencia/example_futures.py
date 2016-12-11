from concurrent.futures import ThreadPoolExecutor
import urllib2
import os
from urls import *


def download_url_into_file(filename, url):
    response = urllib2.urlopen(url)
    fd = file(os.path.join("futures", filename), "w")
    fd.write(response.read())
    fd.close()


procs = []
with ThreadPoolExecutor(max_workers=10) as pool:
    for name, url in urls.items():
        filename = "%s.html" % name
        pool.submit(download_url_into_file, filename, url)

print "Finish!"
