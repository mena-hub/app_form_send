from django.shortcuts import render

from django.conf import settings

from django.utils import timezone

from django.core.mail import EmailMessage

from .form import EmailsForm

def email(request):

     if request.method == 'POST':
         
         form = EmailsForm(request.POST)

         if form.is_valid():

             instance = form.save(commit=False)
             
             email = form.cleaned_data.get('email')
             subject = form.cleaned_data.get('subject')
             message = form.cleaned_data.get('message')
             
             instance.publish_date = timezone.now()
             
             instance.save()
             
             email_from = settings.EMAIL_HOST_USER
             recipient_list = [email]
             email = EmailMessage(subject, message, email_from, recipient_list)
             email.send()

     else:
         
         form = EmailsForm()

     return render(request, 'form/form.html', {'form': form})
