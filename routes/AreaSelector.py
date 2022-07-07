from routes.MailSender import MailSender
from routes.TelegramSender import TelegramSender
from . import routes

@routes.route('/trespass/<area>')
def areaReceiver(area):
    if area == "1":
        content = "Trespassing has been detected in the backyard"
        TelegramSender.telegram_bot_sendtext(content)
        mailingList('EmailIds.txt', content)
        return "Mail Sent for tresspassing in backyard"
    elif area == "2":
        content = "Trespassing has been detected in the portico"
        TelegramSender.telegram_bot_sendtext(content)
        mailingList('EmailIds.txt', content)
        return "Mail Sent for tresspassing in portico"
    else:
        return "No tresspassing detected"


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