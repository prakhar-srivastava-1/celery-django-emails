from celery.decorators import task

# sending feedback to celery
from celery.utils.log import get_task_logger

# import email components
from .emails import send_review_email

# create a logger
logger = get_task_logger(__name__)

# name of the task used in send_email method call
@task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    # send a message to logger
    logger.info("Sent review email")
    # call the method
    return send_review_email(name, email, review)
    
    

