import imaplib
# Para importar variables de entorno
from dotenv import load_dotenv
import email
import traceback

# Cargamos las variables de entorno
# configurar en un futuro para que se carguen en el archivo .env
# load_dotenv(".env")
class EmailService:
    
    def read_email(self):
        try:
            # Conectamos con el servidor
            mail = imaplib.IMAP4_SSL('imap.gmail.com', port=993)
            # Iniciamos sesión. El primer parámetro es el usuario y el segundo la contraseña

            # ingresar aqui mail y usuario
            mail.login('mail', 'password')

            # Nos conectamos a la bandeja de entrada
            mail.select('inbox')
            # Buscamos los correos no leídos
            result, data = mail.search(None, 'SEEN')

            result, data = mail.search(None, '(UNSEEN Subject "%s")' % "Print status")

            print("mostrando data:")
            print(data)

            mail_ids = data[0]

            id_list = mail_ids.split()

            print('Mails list: ', id_list)
            id_list = [b'172']
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