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
    flag_mails_encontrados = email.read_email()
    
    # Si se encontraron correos no leidos se envia un email 
    if flag_mails_encontrados:
        print("Enviando email...")
        email.send_email()
        
    print("Terminando tarea")
    return

