# 6.Write a Python program that reads email details (sender, recipient, subject, and body) 
# from user input and sends the email using Mailtrap as the SMTP server.

import smtplib
from email.mime.text import MIMEText

email_from = input("Enter Your E-mail address :")
email_to = input("Enter recipient's E-mail address :")
subject = input("Enter E-mail subject :")
body = input("Enter E-mail body :")

message = MIMEText(body)
message['From'] = email_from
message['To'] = email_to
message['Subject'] = subject

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'c573a9339a8e77'
EMAIL_HOST_PASSWORD = 'd9792f32dd63dd'
EMAIL_PORT = '2525'

server = smtplib.SMTP(EMAIL_HOST,EMAIL_PORT)
server.starttls()
server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)

server.sendmail(email_from,email_to,message.as_string())
print("Mail sent successfully")
server.quit()