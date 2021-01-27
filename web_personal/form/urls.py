from django.urls import path
from form import views

urlpatterns = [
    path("", views.ContactView.as_view(), name="contact"),
]