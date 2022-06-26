# celery-django-emails
This application will receive user inputs in a form and send an email to the user. Technologies used are Django, Celery and RabbitMQ.

## Dependencies
- Django
- RabbitMQ
- Erlang (for RabbitMQ)
- Celery
- gevent (for Windows)

> pip install django celery gevent
* Setup RabbitMQ server manually

## Architecture
![image](https://user-images.githubusercontent.com/50711734/175800076-44d9809c-fe45-423d-9b1a-18b6cc34d210.png)

## Form
![image](https://user-images.githubusercontent.com/50711734/175800221-297f9ede-363a-4bba-8d15-1288c9bb9b59.png)

## Running the celery app for listening
> celery -A "core" worker -l info -P gevent

![image](https://user-images.githubusercontent.com/50711734/175800038-cdd0fdb9-2af0-4462-a00f-ff28b5b5ab5d.png)

## Result on Celery prompt
![image](https://user-images.githubusercontent.com/50711734/175800051-6ec8baa8-6cca-430f-9ac6-396dd283a998.png)

## Email Received
![image](https://user-images.githubusercontent.com/50711734/175800167-7bccae1d-1d1b-411e-a790-e0b495dda8d4.png)
