from flask import Flask, request
import re

app = Flask(__name__)

class MailingListEditor():

    @app.route('/addEmail', methods = ['GET'])
    def mailAdd():
        name = request.args.get('email')
        if MailingListEditor.check(name):
            with open("EmailIds.txt","a") as file:
                file.write(name)
                file.write("\n")
        else:
            print("Not a Valid Email ID")

        return name

    @app.route('/removeEmail', methods = ['GET'])
    def mailRemove():
        name = request.args.get('email')
        if MailingListEditor.check(name):
            with open("EmailIds.txt", "r") as file:
                lines = file.readlines()

            with open("EmailIds.txt", "w") as file:
                for line in lines:
                    if line.strip("\n") != name:
                        file.write(line)
        else:
            print("Not a Valid Email ID")

        return name
    
    def check(s):
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat,s):
            return True
        return False
    

app.run()