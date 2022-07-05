from routes.MailSender import MailSender
from . import routes

class Mail:
    def __init__(self):
        self.lines = []
        self.content = ""

    @routes.route('/trespass/<area>')
    def interruptReceiver(area):
        mail = Mail()

        if area == "1":
            mail.content = "Trespassing has been detected in the backyard"
            mail.mailingList('EmailIds.txt')
        elif area == "2":
            mail.content = "Trespassing has been detected in the portico"
            mail.mailingList('EmailIds.txt')
        else:
            return "No tresspassing detected"
        return "Mail Sent for tresspassing"


    def mailingList(self,file_path):
        try:
            stopword=open(file_path,"r")
            self.lines = stopword.read().split('\n')
            for i in self.lines:
                print(i)
                mailer = MailSender(i,self.content)
                mailer.send()                    
        except Exception as e:
            print(e)