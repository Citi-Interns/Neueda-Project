from MailSender import MailSender

class Mail:

    def __init__(self):
        self.lines = []
        self.content = ""


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

if __name__ == '__main__':
    mail = Mail()
    mail.mailingList('EmailIds.txt')
