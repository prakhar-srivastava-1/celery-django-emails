from django.urls import path
from .views import ReviewFormView

urlpatterns = [
    path('', ReviewFormView.as_view(), name="review")
]