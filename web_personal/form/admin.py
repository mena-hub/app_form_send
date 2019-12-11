from django.contrib import admin

from django.contrib import admin
from .models import Emails

class EmailsAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'message')

admin.site.register(Emails, EmailsAdmin)
