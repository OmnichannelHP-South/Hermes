import imaplib
# Libreria necesaria para importar las variables de entorno
from dotenv import load_dotenv
import email
import traceback
import os
# Librerias para enviar el correo
from django.conf import settings
from django.core.mail import send_mail
# Libreria para renderizar el template HTML. Documentación: https://docs.djangoproject.com/en/4.1/topics/templates/
from django.template.loader import render_to_string

# Cargamos las variables de entorno
load_dotenv()
class EmailService:
    def read_email(self):
        '''
        Revisa la bandeja de entrada y entre los correos no leidos busca el que tenga el asunto "Print status"

        Si encuentra un correo devuelve un booleano.
        TODO: a futuro pensar en el caso de que se detecten multiples correos no leidos
        '''

        flag_mails_encontrados = False

        try:
            # Conectamos con el servidor
            print("*****Conectando con el servidor*****")
            mail = imaplib.IMAP4_SSL(os.environ.get('SMTP_SERVER'))
            # Iniciamos sesión. El primer parámetro es el usuario y el segundo la contraseña
            mail.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASSWORD'))
            # Nos conectamos a la bandeja de entrada
            mail.select('inbox')
            # Buscamos los emails que contengan el asunto "Print status"
            result, data = mail.search(None, '(UNSEEN Subject "%s")' % "Print status")

            print("mostrando data:")
            print(data)

            mail_ids = data[0]

            id_list = mail_ids.split()
            print('data: ', data)
            print('Mails list (id_list): ', id_list)
            # email de prueba para ver 
            # id_list = [b'172']

            # si id_list no es vacio significa que hay correos no leidos
            if id_list:
                flag_mails_encontrados = True

            for mail_id in id_list:
                result, data = mail.fetch(str(mail_id, encoding='UTF-8'), '(RFC822)')

                for response_part in data:
                    if isinstance(response_part, tuple):
                        # from_bytes, not from_string
                        msg = email.message_from_bytes(response_part[1])
                        email_subject = msg['subject'] 
                        email_from = msg['from']

                        print('email subject: ', email_subject)

                        email_addr = str(email_from).split("\" ")[-1].replace("<", "").replace(">", "")

                        if 'Print status' in email_subject:
                            print('From: ', email_from)
                            print('Email: ', email_addr)
                            print('**********')
                            print(msg.keys())
                                                    
                            print('**********')
                            print(msg)
                                                    

        except Exception as e:
            print("*****Operación fallida*****")
            traceback.print_exc()
            print(str(e))  

        return flag_mails_encontrados

    def send_email(self):
        '''
        Funcion que envia un mail

        TODO: añadir distintas platillas HTML y que estas sean un parametro de la función. Esto pensando en el caso de un email para: "abrir incidente", "asignar técnico", "cerrar incidente", etc.
        '''
        print("Current working directory 1: {0}".format(os.getcwd()))
        mensaje = render_to_string('/django/app/services/templates/Template_mail/ticket.html')


        send_mail(
            subject='Un incidente ha sido generado — Ticket 3291 ',
            message='',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['gonzaloespanah@gmail.com'],
            html_message=mensaje,
        )
        return