from django.views.generic.base import TemplateView
from .emailService import EmailService

class EmailRead(TemplateView):
    template_name = 'mailTest.html'

    def get_context_data(self, **kwargs):
        
        email = EmailService()
        email.read_email()

        context = {'nombre': 'Oscar'}
        return context