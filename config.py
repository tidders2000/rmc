import os
from flask import Flask
import pymysql
from flask_mail import Mail, Message

app = Flask(__name__)

class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") 
    
class BaseConfig(object):
    DEBUG = False
    # shortened for readability
    SECRET_KEY = 'os.getenv("SECRET_KEY") '
    username = os.getenv('C9_USER')
    connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='crowd')  

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
