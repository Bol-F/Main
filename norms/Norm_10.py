import threading
import smtplib
import time
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
PORT = 587
USERNAME = "bolievfirdavs0@gmail.com"
PASSWORD = "vtdqbzgquzipyidz"


def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg["From"] = USERNAME
    msg["To"] = recipient
    msg["Subject"] = subject
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
    recipients = [
        "bolievfirdavs5@gmail.com",
    ]
    subject = "Тестовое письмо"
    body = "Привет! Это письмо отправлено через threading."

    threads = []
    start = time.time()

    for i, rcpt in enumerate(recipients):
        t = threading.Thread(target=send_email, args=(rcpt, subject, body))
        t.start()
        threads.append(t)

        if i < len(recipients) - 1:
            time.sleep(0.5)

    for t in threads:
        t.join()

    elapsed = time.time() - start
    print(f"\nОтправлено писем: {len(recipients)} за {elapsed:.2f} сек.")
