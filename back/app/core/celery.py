import os
from celery import Celery
# el siguiente import es para poder ejecutar el worker de celery cada cierto tiempo
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
# La siguiente linea descubre las tareas dentro de las otras aplicaciones (carpetas), como requirimiento las tareas deben estar dentro de un archivo llamado tasks.py
app.autodiscover_tasks()

# Ejecutar el worker de celery cada cierto tiempo.
# Documentación: https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#crontab-schedules
app.conf.beat_schedule = {
# La tarea reciveEmails se ejecuta cada 30 segundas
'receiveEmails': {
    # run this task every minute
    'task': 'services.tasks.receiveEmails',
    # Para ejecutar cada 1 minuto
    # 'schedule': crontab(),
    # Para ejecutar cada 30 segundos
    'schedule': 5.0,
  }
}

app.conf.timezone = 'America/Santiago'