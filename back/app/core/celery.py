import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
# La siguiente linea descubre las tareas dentro de las otras aplicaciones (carpetas), como requirimiento las tareas deben estar dentro de un archivo llamado tasks.py
app.autodiscover_tasks()