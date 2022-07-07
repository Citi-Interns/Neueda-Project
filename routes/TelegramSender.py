import requests

class TelegramSender:
    def telegram_bot_sendtext(bot_message):

        bot_token = '5435749394:AAHMQrVFj52iqm_LD1T2WNhdAtJkJW7qLEY'
        bot_chatID = '632043567'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)

        return response.json()


    # test = telegram_bot_sendtext("Testing Telegram bot")
    # print(test)