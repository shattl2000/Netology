import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:

    def __init__(self):
        self.SMTP_SERVER = 'smtp.yandex.ru'
        self.IMAP_SERVER = 'imap.yandex.ru'
        self.email_login = 'my_mail_adress@yandex.ru'
        self.password = 'qwerty'
        self.subject = 'Mail from python application'
        self.recipients = ['vasya@email.com', 'petya@email.com']
        self.message = 'Hello my friend!'
        self.header = None

    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.email_login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))
        server = smtplib.SMTP(self.SMTP_SERVER, 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.email_login, self.password)
        server.sendmail(self.email_login, self.recipients, msg.as_string())
        server.quit()

    def recieve(self):
        mail = imaplib.IMAP4_SSL(self.IMAP_SERVER)
        mail.login(self.email_login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header \
            else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email.message_from_string(str(raw_email))
        mail.logout()


if __name__ == '__main__':
    mail = SendEmail()
    mail.send_message()
    mail.recieve()
