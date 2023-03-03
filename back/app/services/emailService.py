import imaplib
# Para importar variables de entorno
from dotenv import load_dotenv
import email
import traceback
import os

# Cargamos las variables de entorno
load_dotenv()
class EmailService:
    
    def read_email(self):
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

            print('Mails list: ', id_list)
            # email de prueba para ver 
            # id_list = [b'172']

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