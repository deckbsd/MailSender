import sendgrid
from sendgrid.helpers.mail import *

class MailSender:

    def __init__(self):
        self._client = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    def send(self, From, To, Subject, Message):
        mail_from = Email(From)
        mail_to = Email(To)
        content = Content("text/plain", Message)
        mail = Mail(mail_from, Subject, mail_to, content)
        response = self._client.client.mail.send.post(request_body=mail.get())
        return response.status_code