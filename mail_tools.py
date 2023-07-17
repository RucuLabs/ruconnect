import imaplib
import time

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
