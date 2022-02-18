from celery import Celery
from celery.utils.log import get_task_logger

# Create the celery app and get the logger
celery_app = Celery('tasks', backend='rpc://',broker='pyamqp://guest@rabbit//')
logger = get_task_logger(__name__)

import time


@celery_app.task
def sample_task():
    return "Hello world"