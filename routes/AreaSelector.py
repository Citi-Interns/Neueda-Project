from routes.MailSender import MailSender
from . import routes

@routes.route('/trespass/<area>')
def areaReceiver(area):
    if area == "1":
        content = "Trespassing has been detected in the backyard"
        mailingList('EmailIds.txt', content)
    elif area == "2":
        content = "Trespassing has been detected in the portico"
        mailingList('EmailIds.txt', content)
    else:
        return "No tresspassing detected"
    return "Mail Sent for tresspassing"


def mailingList(file_path,content):
    try:
        stopword=open(file_path,"r")
        lines = stopword.read().split('\n')
        for i in lines:
            print(i)
            mailer = MailSender(i,content)
            mailer.send()                    
    except Exception as e:
        print(e)