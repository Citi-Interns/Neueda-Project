from routes import *
from flask import Flask

def main():
    app = Flask(__name__)
    app.register_blueprint(routes)
    app.run()

if __name__ == "__main__" :
    main()