from celery.decorators import task

# name of the task used in send_email method call
@task(name="send_review_email_task")
