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
            print(f"[{time.time():.2f}] good.\nRecipient: {recipient}")
    except Exception as e:
        print(f"[{time.time():.2f}] error.\nRecipient: {recipient}\n{e}")


def main():
    recipient = ["bolievfirdavs5@gmail.com"]
    subject = "This message for u!"
    body = "Hello, this message was send via PyCharm"

    threads = []
    start = time.time()

    for i, rcpt in enumerate(recipient):
        t = threading.Thread(target=send_email, args=(rcpt, subject, body))
        t.start()
        threads.append(t)

        if i < len(recipient) - 1:
            time.sleep(0.5)

    for t in threads:
        t.join()

    elapsed = time.time() - start
    print(f"Number of the sand emails: {len(recipient)} in {elapsed:.2f}s")


if __name__ == "__main__":
    main()
