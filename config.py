import os
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") 
    
    
