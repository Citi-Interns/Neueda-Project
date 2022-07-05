from . import routes
import re


@routes.route('/addEmail/<email>')
def mailAdd(email):
    print(email)
    if check(email):
        with open("EmailIds.txt","r") as file:
            loglist = file.readlines()
            file.close()
            found = False
            for line in loglist:
                 if email in line:
                    print("Found it")
                    found = True
                    return "Email Id is already present in Mailing List"

            if not found:
                file = open("EmailIds.txt", "a")
                file.write(email+"\n")
                file.close()
    else:
        print("Not a Valid Email ID")

    return email

@routes.route('/removeEmail/<email>')
def mailRemove(email):
    if check(email):
        with open("EmailIds.txt", "r") as file:
            lines = file.readlines()

        with open("EmailIds.txt", "w") as file:
            for line in lines:
                if line.strip("\n") != email:
                    file.write(line)
                    file.close()
    else:
        print("Not a Valid Email ID")

    return email
    
def check(s):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat,s):
        return True
    return False