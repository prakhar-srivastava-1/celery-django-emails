from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse

from .forms import ReviewForm

# Create your views here.
class ReviewFormView(FormView):
    form_class = 'ReviewForm'
    template_name = 'review.html'

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review!"
        return HttpResponse(msg)