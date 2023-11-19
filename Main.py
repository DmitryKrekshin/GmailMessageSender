import configparser
import smtplib
import sys
from email.mime.text import MIMEText

config = configparser.ConfigParser()
config.read("Config.ini")

subject = config["message"]["subject"]
if len(sys.argv) > 1:
    email_text = sys.argv[1]
else:
    email_text = config["message"]["text"]

GMAIL_USERNAME = config["email_sender"]["userName"]
GMAIL_APP_PASSWORD = config["email_sender"]["password"]

recipients = config["email_receiver"]["email"].split(";")
msg = MIMEText(email_text)
msg["Subject"] = subject
msg["To"] = ", ".join(recipients)
msg["From"] = f"{GMAIL_USERNAME}@gmail.com"

smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
smtp_server.sendmail(msg["From"], recipients, msg.as_string())
smtp_server.quit()
