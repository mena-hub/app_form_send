from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import ContactForm

class ContactView(FormView):
    template_name = "form/contact.html"
    form_class = ContactForm

    def form_valid(self, form):
        try:
            self.send_email(form.cleaned_data)
            messages.success(self.request, 'Envío oka.')
        except:
            messages.error(self.request, 'Envío error.')
        return super(ContactView, self).form_valid(form)

    @staticmethod
    def send_email(valid_data):
        name = valid_data.get('name')
        email = valid_data.get('email')
        content = valid_data.get('content')
        # Inicializar 
        email = EmailMessage(
            "Contacto: Nuevo mensaje",
            "De {} <{}>\n\n{}".format(name, email, content),
            "no-contestar@inbox.mailtrap.io",
            ["mssz.nnia@gmail.com"],
            reply_to=[email],
        )
        email.send()

    def get_success_url(self):
        return reverse_lazy("contact")