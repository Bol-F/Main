import threading
import smtplib
import time
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
PORT        = 587
USERNAME    = 'Firdavs'
PASSWORD    = '2006.08.10.bol'

def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg['From']    = USERNAME
    msg['To']      = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_SERVER, PORT, timeout=10) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(USERNAME, PASSWORD)
            smtp.send_message(msg)
        print(f"[{time.time():.2f}] ✓ Успешно отправлено на {recipient}")
    except Exception as e:
        print(f"[{time.time():.2f}] ✗ Ошибка при отправке {recipient}: {e}")

def main():
    recipients = ['bolievfirdavs5@gmail.com']
    subject = 'Тестовое письмо'
    body    = 'Привет! Это письмо отправлено через threading.'

    threads = []
    start = time.time()
    for rcpt in recipients:
        t = threading.Thread(target=send_email, args=(rcpt, subject, body))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    elapsed = time.time() - start
    print(f"\nОтправлено попыток: {len(recipients)} за {elapsed:.2f} сек.")

if __name__ == '__main__':
    main()
