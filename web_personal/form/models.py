from django.db import models

class Emails(models.Model):
    email = models.EmailField(verbose_name="Correo electrónico")
    subject = models.CharField(max_length=1000, verbose_name="Asunto")
    message = models.TextField(max_length=20000, verbose_name="Mensaje")

    def __str__(self):
        return self.email
