import imaplib
import time
import email

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
            new_mail.append(raw_email)

        imap.logout()
        return new_mail

    except Exception as e:
        print('Error:', str(e))
        return []

def obtain_mail_content(mail_):
    if mail_.is_multipart():
        for part in mail_.iter_parts():
            if part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
                return part.get_payload(decode=True).decode(part.get_content_charset())
    else:
        return mail_.get_payload(decode=True).decode(mail_.get_content_charset())

    return ''

