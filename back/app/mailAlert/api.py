from .models import MailAlert
from rest_framework import viewsets, permissions
from .serializers import MailAlertSerializer

class MailAlertViewSet(viewsets.ModelViewSet):
    queryset = MailAlert.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MailAlertSerializer