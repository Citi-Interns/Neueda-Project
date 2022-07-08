from routes import *
from flask import Flask
import os

def main():
    app = Flask(__name__)
    app.register_blueprint(routes)
    IS_DEV = app.env == 'development'
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='0.0.0.0', port=8081)

if __name__ == "__main__" :
    main()