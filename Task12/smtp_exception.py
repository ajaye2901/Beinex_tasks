#8.write a python program to handle exceptions when sending emails using Python's smtplib library.


import smtplib
from email.mime.text import MIMEText

def mail(email_from,email_to,subject,body) :
        
    try :
        message = MIMEText(body)
        message['From'] = email_from
        message['To'] = ','.join(email_to)
        message['Subject'] = subject

        EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
        EMAIL_HOST_USER = 'c573a9339a8e77'
        EMAIL_HOST_PASSWORD = 'd9792f32dd63ds'
        EMAIL_PORT = '2525'

        server = smtplib.SMTP(EMAIL_HOST,EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)

        server.sendmail(email_from,email_to,message.as_string())
        print("Mail sent successfully")
        server.quit()

    except smtplib.SMTPConnectError :
        print("Error!! SMTP Fail to establish a connection")
    except smtplib.SMTPAuthenticationError :
        print("Error!! Authentication Failed, Enter correct credentials")

email_from = input("Enter Your E-mail address :")
email_to = input("Enter recipient's E-mail address (seperated by comma):").split(',')
subject = input("Enter E-mail subject :")
body = input("Enter E-mail body :")

mail(email_from,email_to,subject,body)