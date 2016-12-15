from example_celery_tasks import *
from urls import *

jobs = []
for name, url in urls.items():
    filename = "%s.html" % name
    jobs.append(download_url_into_file.delay(filename, url))

for job in jobs:
    job.get()
