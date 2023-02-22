from rest_framework import serializers
from .models import MailAlert

class MailAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailAlert
        fields = '__all__'
        read_only_fields = ('created_at',)