import os
from flask import Flask, render_template, redirect, request, url_for, request
import pymysql
from config import Config
from forms import LoginForm





app = Flask(__name__)

app.config['SECRET_KEY'] = 'heffalump_34'
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='crowd')


@app.route('/')
def login():
    form = LoginForm()
    return render_template('index.html', title='Sign In', form=form)

@app.route('/ammend_user')
def get_tasks():
    
    try:
    # Run a query
     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = " SELECT users.id, users.firstname, users.lastname,location.locationname,teamname.teamname FROM users INNER JOIN location ON location.id=users.id INNER JOIN teamname ON teamname.id=users.teamid"
        cursor.execute(sql)
        result = cursor.fetchall()
        
    except:
    # Close the connection, regardless of whether or not the above was successful
     print("An exception occurred")
    
    
    return render_template("ammend_user.html", users=result)

    
    
if __name__=='__main__':
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
    