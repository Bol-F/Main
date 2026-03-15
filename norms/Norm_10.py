import threading
import smtplib
import time
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
PORT = 587
USERNAME = "bolievfirdavs0@gmail.com"
# Use App Password, not regular password
APP_PASSWORD = "xrunlbwikietulgk"  # Replace with actual app password


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
            smtp.login(USERNAME, APP_PASSWORD)  # Use app password
            smtp.send_message(msg)
            print(f"[{time.time():.2f}] ✅ Email sent successfully!")
            print(f"Recipient: {recipient}")
    except smtplib.SMTPAuthenticationError as auth_err:
        print(f"[{time.time():.2f}] 🔒 Authentication failed!")
        print(f"Error: {auth_err}")
        print("\nTroubleshooting steps:")
        print("1. Enable 2-Step Verification: https://myaccount.google.com/security")
        print("2. Generate App Password: https://myaccount.google.com/apppasswords")
        print("3. Use the 16-character app password, not your regular password")
    except Exception as e:
        print(f"[{time.time():.2f}] ❌ Error sending email")
        print(f"Recipient: {recipient}")
        print(f"Error: {e}")


def main():
    recipients = ["bolievfirdavs5@gmail.com"]  # Test with one first
    subject = "This message for u!"
    body = "Hello, this message was sent via Python script"

    threads = []

    for rcpt in recipients:
        t = threading.Thread(target=send_email, args=(rcpt, subject, body))
        t.start()
        threads.append(t)
        time.sleep(1)  # Slightly longer delay

    for t in threads:
        t.join()

    print(f"\nAttempted to send {len(recipients)} emails")


if __name__ == "__main__":
    main()