from __future__ import absolute_import, unicode_literals
# from celery import shared_task
from core.celery import app
from celery.utils.log import get_task_logger
from .emailService import EmailService

logger = get_task_logger(__name__)

@app.task
def receiveEmails():
    print("Iniciando tarea...")
    email = EmailService()
    email.read_email()
    print("Terminando tarea")
    return

