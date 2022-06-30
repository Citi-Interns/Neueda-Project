import smtplib
import ssl
from email.message import EmailMessage

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "neuedaproject2022@gmail.com"
        self.password = "orrnpzczppgbdnjq"

    def send(self, emails_receiver, subject, content):
        em = EmailMessage()
        em['From'] = self.sender_mail
        em['To'] = emails_receiver
        em['Subject'] = subject
        em.set_content(content)


        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context= context) as smtp:
            smtp.login(self.sender_mail,self.password)
            smtp.sendmail(self.sender_mail,emails_receiver,em.as_string())
        # ssl_context = ssl.create_default_context()
        # service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        # service.login(self.sender_mail, self.password)
        
        # for email in emails:
        #     result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        # service.quit()


if __name__ == '__main__':
    mails = input("Enter emails: ").split()
    subject = input("Enter subject: ")
    content = input("Enter content: ")

    mail = Mail()
    mail.send(mails, subject, content)
