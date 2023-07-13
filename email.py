import imaplib
import time

IMAP_HOST = 'imap.ex.com'
IMAP_PORT = 993
USERNAME = 'user@ex.com'
PASSWORD = 'pass'

TIME = 10

def print_email_content(email_data):
    print(email_data)

def check_emails():
    while True:
        try:
            imap = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
            imap.login(USERNAME, PASSWORD)
            imap.select('INBOX')
            status, response = imap.search(None, '(UNSEEN)')
            message_ids = response[0].split()

            for message_id in message_ids:
                status, response = imap.fetch(message_id, '(RFC822)')
                raw_email = response[0][1]
                print_email_content(raw_email)
                imap.store(message_id, '+FLAGS', '\\Seen')

            imap.logout()

        except Exception as e:
            print('Error:', str(e))

        time.sleep(TIME)

check_emails()

