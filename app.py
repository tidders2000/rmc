import os
from flask import Flask, render_template, redirect, request, url_for, request, flash, session, g, jsonify
import pymysql
from config import Config
from forms import LoginForm, SignUp
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images/profile'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object(Config)

mail = Mail(app)
# Connect to the database.........................
username = os.getenv('C9_USER')
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='crowd')
#login form................................

@app.route('/', methods=['GET','POST'])
def login():
    
 form = LoginForm()
 if g.user:
        return render_template('home.html')
 if request.method == 'POST' and form.validate_on_submit():
       session.pop('user', None)
       password=request.form['password']
       email=request.form['email']
       
       
       
       try:
        with connection.cursor() as cursor:
            sql= "SELECT `email` FROM `users` WHERE `email`=%s"
            cursor.execute(sql,(email))
            result = cursor.fetchone()
            
            if result[0] !=email:
              
                return redirect('/')
            
            sql= "SELECT `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql,(email))
            result = cursor.fetchone()
            flash(result[0])
            if check_password_hash(result[0], password):
             session['user'] = request.form['email']
             return redirect('home')
                
       except:
              # Close the connection, regardless of whether or not the above was successful
            flash("incorrect email or password")
          
 return render_template('index.html', form=form)
    
    
#users home screen after signin ...................   
@app.route('/home')

def home():
    
    if g.user:
        page_title = 'Home'
        email=g.user
        try:
            with connection.cursor() as cursor:
                sql= "SELECT `profileImage` FROM `users` WHERE `email`=%s"
                cursor.execute(sql,(g.user))
                session['image'] = cursor.fetchone()
                profilepic=session['image'][0]
                flash(profilepic)
                
        except:
             flash('error')
        
        return render_template('home.html', page_title=page_title, profilepic=profilepic)
   
    
    return redirect('/')
    
@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
    
@app.route('/signup', methods=['GET', 'POST'])

#sign up users to the db.................................
def signup():
 page_title = "Sign Up"    
 form = SignUp()
 if request.method == 'POST' and form.validate_on_submit():
       
       firstname=request.form['firstname']
       lastname=request.form ['lastname']
       password=generate_password_hash(request.form['password'])
       email=request.form['email']
       profileImage='blank_profile.png'
       #check user e mail does not esist
       
       try:
        with connection.cursor() as cursor:
            sql= "SELECT `email` FROM `users` WHERE `email`=%s"
            cursor.execute(sql,(email))
            result = cursor.fetchall()
            flash(result)
            
            if len(result)!=0:
                flash('already registered')
                return redirect('signup')
         # add user to db   
            
            else:
                with connection.cursor() as cursor:
                    sql= "INSERT INTO `users` (`firstname`, `lastname`, `email`, `password`,`profileImage`) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql,(firstname,lastname,email,password,profileImage))
                    connection.commit()
                    flash('data added')
                    session['user'] = request.form['email']
                    return redirect('/mail')
       except:
              # Close the connection, regardless of whether or not the above was successful
            flash("An exception occurred")
          
 return render_template('signup.html', form=form, page_title=page_title)
 
@app.route('/updateInfo')
def get_tasks():
    page_title = "Update Info"
    try:
    # Run a query 
     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = " SELECT users.id, users.firstname, users.lastname,location.locationname,teamname.teamname FROM users INNER JOIN location ON location.id=users.id INNER JOIN teamname ON teamname.id=users.teamid"
        cursor.execute(sql)
        result = cursor.fetchall()
        
    except:
    # Close the connection, regardless of whether or not the above was successful
     print("An exception occurred")
    
    
    return render_template('updateInfo.html', users=result, page_title=page_title)

@app.route("/mail")
def index():
   msg = Message('Hello', sender = 'tidders2000@gmail.com', recipients = [session['user']])
   msg.body = "user sucessfully created for rate my crowd.com"
   mail.send(msg)
   flash('user created')
   session.pop('user', None)
   return redirect('/')
   
@app.route("/logout")
def logout():
    session.pop('user', None)
    print('logged out')
    return redirect('/')
    
@app.route("/feedback")
def feedback():
    if g.user:
        page_title="My Feedback"
        return render_template("feedback.html", page_title=page_title)
    return redirect('/')
    
    
@app.route("/add_feedback")
def add_feedback():
    if g.user:
        page_title="Add Feedback"
        return render_template("add_feedback.html", page_title=page_title)
    return redirect('/')

  
@app.route("/badges")
def badges():
    if g.user:
        page_title="Badges"
        return render_template("badges.html", page_title=page_title)
    return redirect('/')
    
@app.route("/mycharts")
def mycharts():
    if g.user:
        page_title="My Charts"
        return render_template("mycharts.html", page_title=page_title)
    return redirect('/')
    
@app.route("/myprofile", methods=['GET', 'POST'])
def myprofile():
    if g.user:
        page_title="My Profile"
        profilepic=session['image'][0]
        email=session['user']
        
        try:
         with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql= "SELECT * FROM `users` WHERE `email`=%s"
            cursor.execute(sql,(email))
            result = cursor.fetchall()
           
            sql= "SELECT * FROM location;"
            cursor.execute(sql)
            location = cursor.fetchall()
            sql= "SELECT * FROM teamname;"
            cursor.execute(sql)
            teamname = cursor.fetchall()
            
        except:
            flash('error')
        if request.method == 'POST':
                  firstname=request.form['firstname']
                  lastname=request.form['lastname']
                  biog=request.form['biog']
                  team=request.form['teamie']
                  userid=request.form['id']
                  location=request.form['loca']
                  flash(request.form)
                  flash('Your information has been updated ')
                
               
                  try:
                      with connection.cursor(pymysql.cursors.DictCursor) as cursor: 
                          sql="UPDATE users SET firstname=%s, lastname=%s, biog=%s, teamId=%s, locationId=%s where id=%s"
                         
                          cursor.execute(sql,(firstname,lastname,biog,team,location,userid))
                          connection.commit()
                  except:
                        flash('unable to change data')
      
              
                  
        return render_template("myprofile.html", page_title=page_title, result=result, location=location, teamname=teamname, profilepic=profilepic)
        
            
            
            
    return redirect('/')
    

    
@app.route("/help")
def help():
    if g.user:
        page_title="Help"
        return render_template("help.html", page_title=page_title)  
    return redirect('/')
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS  
           
@app.route('/ppupload', methods=['GET', 'POST'])
def upload_file():
    profilepic=session['image'][0]
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           
            try:
                 with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                    sql="UPDATE users SET profileImage=%s WHERE email=%s"
                    cursor.execute(sql,(filename,g.user))
                    connection.commit()
                    flash('data added')
                  
            except:
                flash('error loading pic')
                
                
                
                
            return redirect('home')   
    return render_template('ppupload.html', profilepic=profilepic)
    
@app.route('/names')
def names():
     try:
                 with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                    sql="SELECT firstname FROM users"
                    cursor.execute(sql)
                    connection.commit()
                    names=cursor.fetchall()
                    flash('data added')
     except:
                    flash('error')
                  
     return jsonify(names)
    
if __name__=='__main__':
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
    