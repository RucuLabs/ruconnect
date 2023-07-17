import imaplib
import time
import email
from email.parser import BytesParser

IMAP_PORT = 993

def check_emails(user, password, imap_host):
    try:
        imap = imaplib.IMAP4_SSL(imap_host, IMAP_PORT)
        imap.login(user, password)
        imap.select('INBOX')
        status, response = imap.search(None, '(UNSEEN)')
        message_ids = response[0].split()

        if len(message_ids) == 0:
            imap.logout()
            return []

        new_mail = []

        for message_id in message_ids:
            status, response = imap.fetch(message_id, '(RFC822)')
            raw_email = response[0][1]
            imap.store(message_id, '+FLAGS', '\\Seen')
            mail_ = BytesParser().parsebytes(raw_email)
            email_content = obtain_mail_content(mail_)
            email_sender, email_date, email_subject = obtain_mail_info(mail_)
            email_structured = [email_content, email_sender, email_date, email_subject]
            new_mail.append(email_structured)

        imap.logout()
        return new_mail

    except Exception as e:
        print('Error:', str(e))
        return []

def obtain_mail_content(mail_):

    if mail_.is_multipart():
        for part in mail_.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain' or content_type == 'text/html':
                content = part.get_payload(decode=True).decode(part.get_content_charset())
                return content
    else:
        content = mail_.get_payload(decode=True).decode(email_message.get_content_charset())
        return content

    return ''

def obtain_mail_info(mail_):
    sender = mail_['From']
    date = mail_['Date']
    subject = mail_['Subject']
    return sender, date, subject

