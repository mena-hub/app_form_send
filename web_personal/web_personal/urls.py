from django.contrib import admin
from django.urls import path
from form import views

urlpatterns = [
    path('', views.email, name='email'),
    path('admin/', admin.site.urls),
]