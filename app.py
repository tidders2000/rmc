import os
import pymysql
from flask import Flask, render_template, redirect, request, url_for, request



app = Flask(__name__)

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='crowd')


@app.route('/')
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
    