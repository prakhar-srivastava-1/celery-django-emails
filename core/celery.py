# default import
from __future__ import absolute_import, unicode_literals
import os

# import Celery
from celery import Celery

# setup settings config 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# instantiate Celery
app = Celery('core')

app.autodiscover_tasks()

# debug info
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request}')