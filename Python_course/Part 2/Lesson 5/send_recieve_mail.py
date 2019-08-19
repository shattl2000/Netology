import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:

    def __init__(self):
        pass

    def send_message(self, email_login, recipients, subject, message,
                     password, smtp_server='smtp.yandex.ru'):
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        server.login(email_login, password)
        msg = MIMEMultipart()
        msg['From'] = email_login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        server.sendmail(email_login, recipients, msg.as_string())
        server.quit()
        print('Email send')

    def recieve(self, email_login, password,
                imap_server='imap.yandex.ru', header=None):
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_login, password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email.message_from_string(str(raw_email))
        mail.logout()


def main():
    while True:
        sender_email = input('Введите ваш e-mail отправителя: ')
        if '@' and '.' in sender_email:
            password = input('Введите пароль: ')
            while True:
                print('Для отправки сообщения введите "send", '
                      'для чтения по заголовку введите "recieve",'
                      ' для выхода введите "exit"')
                to_do = input('Введите команду:')
                if to_do == 'send':
                    recipients_list = list(
                        map(str, input('Введите получателей: ').split(', '))
                    )
                    subject = str(input('Введите тему сообщения: '))
                    message = str(input('Введите сообщение:'))
                    send_email = SendEmail()
                    send_email.send_message(
                        email_login=sender_email,
                        recipients=recipients_list,
                        subject=subject,
                        message=message,
                        password=password,
                    )
                    break
                elif to_do == 'recieve':
                    header = input('Введите заголовок письма')
                    send_email = SendEmail()
                    send_email.recieve(
                        email_login=sender_email,
                        password=password,
                        header=header,
                    )
                    break
                elif to_do == 'exit':
                    print('Выход')
                    break
                else:
                    print('Команда введена неверно!')
            break
        else:
            print('Вы ввели некорректный e-mail, попробуйте еще раз! : ')


if __name__ == '__main__':
    main()
