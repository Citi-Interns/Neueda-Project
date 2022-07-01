import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

class MailSender:

    def __init__(self,email_receiver,content):
        ####################################################################################
        # "IMPORTANT: WHEN SENDING EMAILS FROM GMAI ENSURE THAT YOU HAVE ENABLED LESS SECURE APPS "
        self.send_from =  "Neueda Test"
        self.send_to = email_receiver
        self.subject = "alert mail for Trespassing in your prohibited area"
        self.body = content
        self.username  =  "neuedaproject2022"
        self.password =  "orrnpzczppgbdnjq"
        # attachmentPath  = "C:\Users\hp\Dropbox\PC\Desktop\Let.txt"          
        ####################################################################################
    def send(self):
        msg = MIMEMultipart()
        msg['From'] = self.send_from
        msg['To'] = self.send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = self.subject
        server = "smtp.gmail.com"
        port = 587
        use_tls = True

        msg.attach(MIMEText(self.body))
        #msg.attach(MIMEText(emailBody ,'html'))

        #### ATTACHMENT CODE ***** COMMENT OUT CODE BELOW TO EXCLUDE ATTACHMENT *******
        # '''
        # part = MIMEBase('application', "octet-stream")
        # with open(attachmentPath, 'rb') as file:
        #     part.set_payload(file.read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition',
        #                 'attachment; filename="{}"'.format(Path(attachmentPath).name))
        # msg.attach(part)
        # '''
        #### COMMENT OUT CODE ABOVE TO EXCLUDE ATTACHMENT *******

        smtp = smtplib.SMTP(server, port)
        if use_tls:
            smtp.starttls()
        smtp.login(self.username, self.password)
        smtp.sendmail(self.send_from, self.send_to, msg.as_string())
        smtp.quit()

        print ("Message Sent")