import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "aryanraj78089@gmail.com"
APP_PASSWORD = " 1234 5678 9123 "
RECEIVER = "gourav8789259854@gmail.com"

msg = EmailMessage()
msg["FROM"] = EMAIL
msg["TO"] = RECEIVER
msg["SUBJECT"] = "GANDU GOURAV"
msg.set_content("HELLO BRO ")
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.sendmail(EMAIL, RECEIVER, msg.as_string())