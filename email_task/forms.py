from django import forms
from .tasks import send_review_email_task

class ReviewForm(forms.Form):
    name = forms.CharField(
        label='Name',
        min_length=4,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Name',
                'id': 'name-field'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Email',
                'id': 'email-field'
            }
        )
    )
    review = forms.CharField(
        label='Review',
        min_length=4,
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5',
            }
        )
    )

    def send_email(self):
        # call the task
        send_review_email_task.delay(
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            self.cleaned_data['review']
        )