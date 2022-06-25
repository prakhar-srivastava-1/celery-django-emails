# Context will help us in passing dictionary to our email_message.txt file
# We will be able to use the keys to get the values there
from email.message import EmailMessage
from django.template import Context

# render_to_string will render the data fetched from email_message.txt file
# as a string with the required variables evaluated and embedded in it
from django.template.loader import render_to_string

# import secrets
from .secrets import EMAIL_ID, PASSWORD

def send_review_email(name, email, review):
    # This dictionary will be passed to email_message.txt
    context = {
        'name': name,
        'email': email,
        'review': review,
    }

    # Django Email work flow:
    #   - Email Subject
    #   - Email Body

    # Subject
    email_subject = "Thanks for your review!"

    # Email Body
    email_body = render_to_string("email_message.txt", context)

    email = EmailMessage(
        email_subject,
        email_body,
        # Source Email
        EMAIL_ID,
        # Target Email - format as per Django doc
        [email, ],
    )

    # send the EmailMessage
    return email.send(fail_silently=False)