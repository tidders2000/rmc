import os
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") 
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    

    