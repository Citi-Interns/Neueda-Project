from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class AddMails(Resource):

    def __init__(self):
        self.name = "niharikamadke@gmail.com"
    def post(self):
        with open("EmailIds.txt","a") as file:
            file.write("\n")
            file.write(self.name)

class RemoveMails(Resource):
    def __init__(self):
        self.name = "niharikamadke@gmail.com"
    def delete(self):
        with open("EmailIds.txt", "r") as file:
            lines = file.readlines()

        with open("EmailIds.txt", "w") as file:
            for line in lines:
                if line.strip("\n") != self.name:
                    file.write(line)

api.add_resource(AddMails(), '/addMails')
api.add_resource(RemoveMails, '/removeMails')


app.run()