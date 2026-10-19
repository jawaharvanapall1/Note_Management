
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER_EMAIL = os.environ.get("EMAIL_ADDRESS")
PASSKEY = os.environ.get("EMAIL_APP_PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


def emailSend(to_email: str, subject: str, body: str):
    if not SENDER_EMAIL or not PASSKEY:
        print("Email credentials are not configured.")
        return False

    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=20) as server:
            server.starttls()
            server.login(SENDER_EMAIL, PASSKEY)
            server.send_message(msg)

        return True

    except Exception as e:
        print("Email sending failed:", e)
        return False
